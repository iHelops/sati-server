from models import User


class MinifiedUserDto:
    def __init__(self, model):
        self.id = str(model.id)
        self.name = model.name
        self.avatar = model.avatar
        self.verified = model.verified

        subscribed_users = User.objects(subscriptions=model)
        self.subscribers = len(subscribed_users)

    def get_dict(self):
        return self.__dict__
