import bson.objectid
from bson import ObjectId
from dtos import PostDto
from exceptions import ApiError
from models import Post, User
from datetime import datetime


def create(user_id: str, content: str, attachments: list):
    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    post = Post(
        author=user,
        content=content,
        attachments=attachments,
        created_at=datetime.now()
    )
    post.save()

    return PostDto(post).get_dict()


def delete(user_id: str, post_id: str):
    post = Post.objects(author=user_id, id=post_id).first()
    if not post:
        raise ApiError.BadRequest('Post not found')

    post.delete()


def like(user_id: str, post_id: str):
    user = User.objects(id=user_id).first()
    post = Post.objects(id=post_id).first()
    if not post:
        raise ApiError.BadRequest('Post not found')
    if not user:
        raise ApiError.BadRequest('User not found')

    for u in post.likes:
        if u == user:
            return

    post.update(push__likes=user)


def unlike(user_id: str, post_id: str):
    post = Post.objects(id=post_id, likes=user_id).first()
    if not post:
        return

    post.update(pull__likes=ObjectId(user_id))


def get_posts(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise ApiError.BadRequest('User not found')

    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    posts = Post.objects(author=user).order_by('-created_at')
    posts_list = [PostDto(post).get_dict() for post in posts]
    return posts_list


def get_lasts():
    posts = Post.objects().order_by('-created_at').limit(10)
    posts_list = [PostDto(post).get_dict() for post in posts]
    return posts_list
