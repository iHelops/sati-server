from flask import Blueprint, redirect
from exceptions import ApiError
from service import user_service

activate_router = Blueprint('activate', __name__, url_prefix='/api')


@activate_router.get('/user/activate/<key>')
def activate(key):
    try:
        user_service.activate(key)
    except ApiError.ApiError:
        pass

    return redirect('/')
