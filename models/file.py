from mongoengine import Document, StringField, ReferenceField
from .user import User


class File(Document):
    author = ReferenceField(User)
    filename = StringField(required=True)
    hash = StringField(required=True)
    type = StringField(required=True)
