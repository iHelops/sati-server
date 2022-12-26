from mongoengine import Document, ReferenceField, StringField, DateTimeField
from .user import User
from .post import Post


class Comment(Document):
    author = ReferenceField(User, required=True)
    post = ReferenceField(Post, required=True)
    content = StringField(required=True)
    created_at = DateTimeField(required=True)
