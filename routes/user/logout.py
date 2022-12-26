from flask import Blueprint, make_response, Response

logout_router = Blueprint('logout', __name__, url_prefix='/api')


@logout_router.post('/user/logout')
def logout():
    res = make_response(Response(status=200))
    res.set_cookie('session', '', httponly=True)
    return res
