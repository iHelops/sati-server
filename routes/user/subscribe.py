from flask import Blueprint, request, Response, jsonify
from webargs import flaskparser, fields
from service import user_service
from decorators import login_required

subscribe_router = Blueprint('subscribe', __name__, url_prefix='/api')

fields_model = {
    'user_id': fields.String(required=True)
}


@subscribe_router.route('/user/subscribe', methods=['POST'])
@login_required
def subscribe(user):
    data = flaskparser.parser.parse(fields_model, request)
    user_data = user_service.subscribe(str(user.id), data['user_id'])
    return jsonify(user_data)
