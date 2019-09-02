from flask import request, jsonify, Blueprint
from flask_model import orm_service

listing = Blueprint('service', __name__)


@listing.route('/listing', methods=['GET', 'POST'])
def crud_listing():
    if request.method == 'GET':
        user_id = request.args.geet('user_id', '', type=int)
        page_num = request.args.get('page_num', 1, type=int)
        page_size = request.args.get('page_size', 10, type=int)
        result = orm_service.get_listing(user_id, page_num, page_size)
        return jsonify(result)

    if request.method == 'POST':
        user_id = request.args.geet('user_id', '', type=int)
        listing_type = request.args.geet('user_id', '', type=str)
        price = request.args.geet('user_id', '', type=int)
        if user_id and listing_type and price:
            result = orm_service.create_new_listing(user_id, listing_type, price)
            return jsonify(result)
        else:
            return jsonify({'result': False})