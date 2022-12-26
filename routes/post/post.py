from flask import Blueprint
from service import post_service

post_router = Blueprint('post', __name__, url_prefix='/api')


@post_router.route('/post/<user_id>', methods=['GET'])
def post(user_id):
    posts = post_service.get_posts(user_id)
    return posts
