# user
from .user.activate import activate_router
from .user.auth import auth_router
from .user.check import check_router
from .user.register import register_router
from .user.subscribe import subscribe_router
from .user.unsubscribe import unsubscribe_router
from .user.user import user_router
from .user.logout import logout_router
from .user.search import search_router
from .user.change_avatar import change_avatar_router

# post
from .post.create import post_create_router
from .post.delete import post_delete_router
from .post.like import post_like_router
from .post.unlike import post_unlike_router
from .post.last import post_last_router
from .post.post import post_router

# comment
from .comment.create import comment_create_router
from .comment.delete import comment_delete_router
from .comment.comment import comment_router

# file
from .file.upload_image import upload_image_router
from .file.file import file_router

# admin
from .admin.delete_post import admin_post_delete_router

routes = [
    activate_router,
    auth_router,
    check_router,
    register_router,
    subscribe_router,
    unsubscribe_router,
    user_router,
    logout_router,
    search_router,
    change_avatar_router,

    post_create_router,
    post_delete_router,
    post_like_router,
    post_unlike_router,
    post_last_router,
    post_router,

    comment_create_router,
    comment_delete_router,
    comment_router,

    upload_image_router,
    file_router,

    admin_post_delete_router
]
