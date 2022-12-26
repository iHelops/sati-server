from flask import Blueprint
from service import user_service

user_router = Blueprint('user', __name__, url_prefix='/api')


@user_router.route('/user/<user_id>', methods=['GET'])
def profile(user_id):
    user_data = user_service.get_user(user_id)
    return user_data
