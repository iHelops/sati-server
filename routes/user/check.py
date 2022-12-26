from flask import Blueprint, jsonify, request
from exceptions import ApiError
from service import user_service

check_router = Blueprint('check', __name__, url_prefix='/api')


@check_router.get('/user/check')
def check():
    session = request.cookies.get('session')
    if not session:
        raise ApiError.UnauthorizedError()

    user_data = user_service.check_auth(session)
    return jsonify(user_data)
