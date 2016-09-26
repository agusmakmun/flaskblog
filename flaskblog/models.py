import datetime
from flask import url_for
from flask_peewee.utils import slugify

from flaskblog import db


class Tag(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, default='none')

    def get_absolute_url(self):
        return url_for('create_tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Post(db.DynamicDocument):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, default='none')
    body = db.StringField(required=True)
    tags = db.ListField(db.ReferenceField('Tag'), default=[])
    created_date = db.DateTimeField(default=datetime.datetime.now, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    @property
    def post_type(self):
        return self.__class__.__name__

    meta = {
        'indexes': ['-created_date', 'title', 'slug', 'tags'],
        'ordering': ['-created_date']
    }
