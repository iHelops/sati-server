from flask import Blueprint, jsonify
from werkzeug.datastructures import FileStorage
from decorators import login_required, file_required
from service import file_service
from service import user_service

change_avatar_router = Blueprint('change_avatar', __name__, url_prefix='/api')
IMAGE_EXT = ['jpeg', 'jpg', 'png']


@change_avatar_router.route('/user/change-avatar', methods=['POST'])
@login_required
@file_required(extensions=IMAGE_EXT, max_size=2)
def change_avatar_image(file: FileStorage, user):
    answer = file_service.upload(str(user.id), file, file_type='avatar')
    user_service.change_avatar(str(user.id), answer['file_id'])
    return jsonify({'avatar_id': answer['file_id']})
