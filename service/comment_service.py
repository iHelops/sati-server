from exceptions import ApiError
from models import Comment, Post, User
from datetime import datetime
from dtos import CommentDto


def create(user_id: str, post_id: str, content: str):
    post = Post.objects(id=post_id).first()
    user = User.objects(id=user_id).first()
    if not post:
        raise ApiError.BadRequest('Post not found')
    if not user:
        raise ApiError.BadRequest('User not found')

    comment = Comment(
        author=user,
        post=post,
        content=content,
        created_at=datetime.now()
    )
    comment.save()

    return CommentDto(comment).get_dict()


def delete(user_id: str, comment_id: str):
    comment = Comment.objects(id=comment_id, author=user_id)
    if not comment:
        raise ApiError.BadRequest('Comment not found')

    comment.delete()


def get_comments(post_id: str):
    comments = Comment.objects(post=post_id)
    comments_list = [CommentDto(comm).get_dict() for comm in comments]
    return comments_list


