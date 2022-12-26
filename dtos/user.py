from models import User
from .minified_user import MinifiedUserDto


class UserDto:
    def __init__(self, model):
        self.id = str(model.id)
        self.email = model.email
        self.name = model.name
        self.avatar = model.avatar
        self.subscriptions = [MinifiedUserDto(sub).get_dict() for sub in model.subscriptions]
        self.verified = model.verified
        self.activated = model.activated
        self.role = model.role

        subscribed_users = User.objects(subscriptions=model)
        self.subscribers = [MinifiedUserDto(sub).get_dict() for sub in subscribed_users]

    def get_dict(self):
        return self.__dict__
