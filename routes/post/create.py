from flask import Blueprint, request
from webargs import flaskparser, fields
from service import post_service
from decorators import login_required

post_create_router = Blueprint('post_create', __name__, url_prefix='/api')

fields_model = {
    'content': fields.String(required=True),
    'attachments': fields.List(fields.String(), missing=[], )
}


@post_create_router.route('/post/create', methods=['POST'])
@login_required
def create(user):
    data = flaskparser.parser.parse(fields_model, request)
    post = post_service.create(str(user.id), data['content'], data['attachments'])
    return post
