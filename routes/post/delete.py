from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import post_service
from decorators import login_required

post_delete_router = Blueprint('post_delete', __name__, url_prefix='/api')

fields_model = {
    'post_id': fields.String(required=True)
}


@post_delete_router.route('/post/delete', methods=['DELETE'])
@login_required
def delete(user):
    data = flaskparser.parser.parse(fields_model, request)
    post_service.delete(str(user.id), data['post_id'])
    return Response(status=204)
