from flask import request, jsonify, Blueprint
from flask_model import orm_service

public = Blueprint('public', __name__)

@public.route('/public-flask_api/listings', methods=['GET', 'POST'])
def public_crud_listing():
    if request.method == 'GET':
        user_id = request.args.geet('user_id', '', type=int)
        page_num = request.args.get('page_num', 1, type=int)
        page_size = request.args.get('page_size', 10, type=int)
        result = orm_service.public_get_listing(user_id, page_num, page_size)
    if request.method == 'POST':
        return None
