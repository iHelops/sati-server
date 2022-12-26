from .minified_user import MinifiedUserDto
from models import Comment


class PostDto:
    def __init__(self, model):
        self.id = str(model.id)
        self.author = MinifiedUserDto(model.author).get_dict()
        self.content = model.content
        self.attachments = model.attachments
        self.created_at = model.created_at
        self.likes = [MinifiedUserDto(like).get_dict() for like in model.likes]

        post_comments = Comment.objects(post=model)
        self.comments = len(post_comments)

    def get_dict(self):
        return self.__dict__
