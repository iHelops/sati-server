from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import user_service
from decorators import login_required

unsubscribe_router = Blueprint('unsubscribe', __name__, url_prefix='/api')

fields_model = {
    'user_id': fields.String(required=True)
}


@unsubscribe_router.route('/user/unsubscribe', methods=['POST'])
@login_required
def unsubscribe(user):
    data = flaskparser.parser.parse(fields_model, request)
    user_service.unsubscribe(str(user.id), data['user_id'])
    return Response(status=200)
