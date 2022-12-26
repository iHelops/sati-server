from flask import Blueprint, request, jsonify
from webargs import flaskparser, fields
from service import user_service

search_router = Blueprint('search', __name__, url_prefix='/api')

fields_model = {
    'query': fields.String(required=True)
}


@search_router.route('/user/search', methods=['POST'])
def search():
    data = flaskparser.parser.parse(fields_model, request)
    if data['query'] == '':
        return jsonify([])

    search_data = user_service.search(data['query'])
    return jsonify(search_data)
