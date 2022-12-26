from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import post_service
from decorators import login_required, admin_required

admin_post_delete_router = Blueprint('admin_post_delete', __name__, url_prefix='/api')

fields_model = {
    'user_id': fields.String(required=True),
    'post_id': fields.String(required=True)
}


@admin_post_delete_router.route('/admin/post/delete', methods=['DELETE'])
@login_required
@admin_required
def admin_post_delete(user):
    data = flaskparser.parser.parse(fields_model, request)
    post_service.delete(data['user_id'], data['post_id'])
    return Response(status=204)
