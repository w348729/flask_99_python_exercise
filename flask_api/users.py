from flask import request, jsonify, Blueprint
from flask_model import orm_service

users = Blueprint('users', __name__)


@users.route('/users/<int:user_id>', methods=['GET'])
def list_one_user(user_id):
    if user_id:
        # get one user
        result = orm_service.get_one_user(user_id)
        return jsonify(result)
    else:
        return jsonify({'false': ' please input valid param'})


@users.route('/users', methods=['GET', 'POST'])
def crud_users():
    if request.method == 'GET':
        page_num = request.args.get('page_num', 1, type=int)
        page_size = request.args.get('page_size', 10, type=int)
        result = orm_service.list_all_users(page_num, page_size)
        return jsonify(result)
    if request.method == 'POST':
        name = request.json
        if name:
            result = orm_service.create_new_user(name)
        else:
            return jsonify({'false': ' please input valid param'})


