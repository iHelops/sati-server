from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import post_service
from decorators import login_required

post_unlike_router = Blueprint('unpost_like', __name__, url_prefix='/api')

fields_model = {
    'post_id': fields.String(required=True)
}


@post_unlike_router.route('/post/unlike', methods=['POST'])
@login_required
def like(user):
    data = flaskparser.parser.parse(fields_model, request)
    post_service.unlike(str(user.id), data['post_id'])
    return Response(status=200)
