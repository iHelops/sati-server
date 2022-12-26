from flask import Blueprint
from service import comment_service

comment_router = Blueprint('comment', __name__, url_prefix='/api')


@comment_router.route('/comment/<post_id>', methods=['GET'])
def comment(post_id):
    posts = comment_service.get_comments(post_id)
    return posts
