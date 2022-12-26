from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import comment_service
from decorators import login_required

comment_delete_router = Blueprint('comment_delete', __name__, url_prefix='/api')

fields_model = {
    'comment_id': fields.String(required=True)
}


@comment_delete_router.route('/comment/delete', methods=['DELETE'])
@login_required
def delete(user):
    data = flaskparser.parser.parse(fields_model, request)
    comment_service.delete(str(user.id), data['comment_id'])
    return Response(status=204)
