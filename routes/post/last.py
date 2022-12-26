from flask import Blueprint
from service import post_service

post_last_router = Blueprint('post_last', __name__, url_prefix='/api')


@post_last_router.route('/post/last', methods=['GET'])
def post():
    posts = post_service.get_lasts()
    return posts
