from flask import Blueprint, jsonify, request, make_response
from webargs import flaskparser, fields
from service import user_service

register_router = Blueprint('register', __name__, url_prefix='/api')

fields_model = {
    'email': fields.Email(required=True),
    'name': fields.String(required=True),
    'password': fields.String(required=True)
}


@register_router.route('/user/register', methods=['POST'])
def register():
    data = flaskparser.parser.parse(fields_model, request)
    user_data = user_service.registration(data['email'], data['name'], data['password'])
    res = make_response(jsonify(user_data))
    res.set_cookie('session', user_data['session'], httponly=True)
    return res
