from flask import Blueprint, request, Response
from webargs import flaskparser, fields
from service import comment_service
from decorators import login_required

comment_create_router = Blueprint('comment_create', __name__, url_prefix='/api')

fields_model = {
    'post_id': fields.String(required=True),
    'content': fields.String(required=True)
}


@comment_create_router.route('/comment/create', methods=['POST'])
@login_required
def create(user):
    data = flaskparser.parser.parse(fields_model, request)
    comment = comment_service.create(str(user.id), data['post_id'], data['content'])
    return comment
