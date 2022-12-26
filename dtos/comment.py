from .minified_user import MinifiedUserDto


class CommentDto:
    def __init__(self, model):
        self.id = str(model.id)
        self.author = MinifiedUserDto(model.author).get_dict()
        self.content = model.content
        self.created_at = model.created_at

    def get_dict(self):
        return self.__dict__
