from flask import request
from exceptions import ApiError
from models import User


def login_required(fn):
    def wrapper(*args, **kwargs):
        session = request.cookies.get('session')
        if not session:
            raise ApiError.UnauthorizedError()

        user = User.objects(sessions=session).first()
        if user is None:
            raise ApiError.UnauthorizedError()

        return fn(user, *args, **kwargs)

    return wrapper
