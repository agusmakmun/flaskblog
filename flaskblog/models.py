import datetime
from flask import url_for
from flask_peewee.utils import slugify

from flaskblog import db

class Tag(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug  = db.StringField(max_length=255, required=True, default='none')

    def get_absolute_url(self):
        return url_for('create_tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Post(db.DynamicDocument):
    title = db.StringField(max_length=255, required=True)
    slug  = db.StringField(max_length=255, required=True, default='none')
    body  = db.StringField(required=True)
    tags  = db.ListField(db.ReferenceField('Tag'), default=[])
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
        'indexes' : ['-created_date', 'title', 'slug', 'tags'],
        'ordering': ['-created_date']
    }




'''

> mongo
use dbName;
db.dropDatabase();
exit

$ mongo
> use flaskblog;
> db.tag.getIndexes()
> db.tag.dropIndexes()



import re
_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')
def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    
    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)
'''