from mongoengine import Document, ReferenceField, StringField, ListField, DateTimeField
from .user import User


class Post(Document):
    author = ReferenceField(User, required=True)
    content = StringField(required=True)
    attachments = ListField(StringField())
    created_at = DateTimeField(required=True)
    likes = ListField(ReferenceField(User))
