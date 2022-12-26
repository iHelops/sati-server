from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import post_service
from decorators import login_required

post_like_router = Blueprint('post_like', __name__, url_prefix='/api')

fields_model = {
    'post_id': fields.String(required=True)
}


@post_like_router.route('/post/like', methods=['POST'])
@login_required
def like(user):
    data = flaskparser.parser.parse(fields_model, request)
    post_service.like(str(user.id), data['post_id'])
    return Response(status=200)
