from flask import (Blueprint, request, redirect, render_template, url_for)
from flask.views import MethodView
from flask_mongoengine.wtf import model_form
from flask_mongoengine.pagination import Pagination

from flaskblog.auth import requires_auth
from flaskblog.models import (Post, Tag)
from flaskblog import config

admin = Blueprint('admin', __name__, template_folder='templates')

class TagView(MethodView):
    decorators = [requires_auth]

    def get_context(self, slug=None):
        if slug:
            tag = Tag.objects.get_or_404(slug=slug)
            form_class = model_form(Tag)
            if request.method == 'POST':
                form = form_class(request.form, initial=tag._data)
            else:
                form = form_class(obj=tag)
        else:
            tag = Tag()
            form_class = model_form(Tag)
            form = form_class(request.form)

        context = {
            'tag' : tag,
            'form': form,
            'create_tag': slug is None,
            'tags': Tag.objects.all()
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('admin/tag.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')
        if form.validate():
            tag = context.get('tag')
            form.populate_obj(tag)
            tag.save()
            return redirect(url_for('admin.create_tag'))

        return render_template('admin/tag.html', **context)


class List(MethodView):
    decorators = [requires_auth]

    def get(self, page=1):
        posts = Post.objects.paginate(page=page, per_page=config.per_page)
        return render_template('admin/list.html', posts=posts, pagination=posts)


class Detail(MethodView):
    decorators = [requires_auth]

    def get_context(self, slug=None):
        if slug:
            post = Post.objects.get_or_404(slug=slug)
            form_class = model_form(Post, exclude=('created_date',))
            if request.method == 'POST':
                form = form_class(request.form, initial=post._data)
            else:
                form = form_class(obj=post)
        else:
            post = Post()
            form_class = model_form(Post, exclude=('created_date',))
            form = form_class(request.form)

        context = {
            'post'  : post,
            'form'  : form,
            'create': slug is None
        }

        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('admin/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')
        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()
            return redirect(url_for('admin.index'))

        return render_template('admin/detail.html' **context)


class DeletePost(MethodView):
    decorators = [requires_auth]

    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        post.delete()

        return redirect(url_for('admin.index'))


class DeleteTag(MethodView):
    decorators =[requires_auth]

    def get(self, slug):
        tag = Tag.objects.get_or_404(slug=slug)
        tag.delete()

        return redirect(url_for('admin.create_tag'))


class Logout(MethodView):

    def get(self):
        # Returning basic http authentication for logout.
        return (''' <p align="center">You are Logout ...</p>
                    <meta http-equiv="refresh" content="2; url=/" />
                ''', 401)


admin.add_url_rule('/logout/', view_func=Logout.as_view('logout'))
admin.add_url_rule('/admin/', view_func=List.as_view('index'))
admin.add_url_rule('/admin/page/<int:page>/', view_func=List.as_view('page'))
admin.add_url_rule('/admin/post/create/', defaults={'slug': None}, view_func=Detail.as_view('create'))
admin.add_url_rule('/admin/post/edit/<slug>/', view_func=Detail.as_view('edit'))
admin.add_url_rule('/admin/post/delete/<slug>/', view_func=DeletePost.as_view('delete'))
admin.add_url_rule('/admin/tag/', defaults={'slug': None}, view_func=TagView.as_view('create_tag'))
admin.add_url_rule('/admin/tag/edit/<slug>/', view_func=TagView.as_view('edit_tag'))
admin.add_url_rule('/admin/tag/delete/<slug>/', view_func=DeleteTag.as_view('delete_tag'))