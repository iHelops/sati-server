from mongoengine import StringField, EmailField, BooleanField, ReferenceField, Document, ListField


class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(required=True)
    avatar = StringField(null=True)
    role = StringField(required=True, default='user')
    subscriptions = ListField(ReferenceField('self'), default=[])
    password = StringField(required=True)
    verified = BooleanField(default=False)
    activated = BooleanField(default=False)
    activation_key = StringField(null=True)
    sessions = ListField(StringField(), default=None, null=True)
