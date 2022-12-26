from flask import Blueprint, jsonify, request, make_response
from webargs import flaskparser, fields
from service import user_service

auth_router = Blueprint('auth', __name__, url_prefix='/api')

fields_model = {
    'email': fields.Email(required=True),
    'password': fields.String(required=True)
}


@auth_router.route('/user/auth', methods=['POST'])
def auth():
    data = flaskparser.parser.parse(fields_model, request)
    user_data = user_service.login(data['email'], data['password'])
    res = make_response(jsonify(user_data))
    res.set_cookie('session', user_data['session'], httponly=True)
    return res
