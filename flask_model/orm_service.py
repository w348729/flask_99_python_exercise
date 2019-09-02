from flask_model.orm_object import Users, Listing
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc
from . import db
import time
import copy

# users
def list_all_users(page_num, page_size):
    try:
        user_list = []
        pagination = Users.query.paginate(page_num, per_page=page_size, error_out=False)
        for each in pagination.items:
            user_list.append(each.to_json())
        if user_list:
            return user_return(True, user_list)
        else:
            return user_return(False, user_list)
    except BaseException as e:
        return user_return(False, [])


def get_one_user(user_id):
    try:
        user_detail = Users.query.filter_by(user_id=user_id).first()
        if user_detail:
            return user_return(True, user_detail.to_json())
    except BaseException as e:
        return user_return(False, '')


def create_new_user(name):
    try:
        new_user = Users(
            name=name['name'],
            created_at=int(time.time() * 1e6),
            updated_at=int(time.time() * 1e6),
        )
        db.session.add(new_user)
        db.session.flush()
    except BaseException as e:
        return {'result': False}
    else:
        session_commit()
        return listing_return(True, new_user.to_json())


# listing
def get_listing(user_id, page_num, page_size):
    try:
        listing = []
        if user_id:
            pagination = Listing.query.filter_by(user_id=user_id).paginate(page_num, per_page=page_size,
                                                                           error_out=False)
            for each in pagination.items():
                listing.append(each.to_json())
            return listing(True, listing)

        else:
            pagination = Listing.query.paginate(page_num, per_page=page_size, error_out=False)
            for each in pagination.items():
                listing.append(each.to_json())
            return listing(True, listing)
    except BaseException as e:
        return listing_return(False, [])


def create_new_listing(user_id, listing_type, price):
    try:
        new_listing = Listing(
            user_id=user_id,
            price=price,
            listing_type=listing_type,
            created_at=int(time.time() * 1e6),
            updated_at=int(time.time() * 1e6),
        )
        db.session.add(new_listing)
        db.session.flush()
    except BaseException as e:
        return {'result': False}
    else:
        session_commit()
        return listing_return(True, new_listing.to_json())


# public
def public_get_listing(user_id, page_num, page_size):
    try:
        listing = []
        result = {
            "id": '',
            "listing_type": '',
            "price": '',
            "created_at": '',
            "updated_at": '',
            "user": {
                "id": '',
                "name": '',
                "created_at": '',
                "updated_at": '',
            }
        }
        if user_id:
            pagination = Listing.query.filter_by(user_id=user_id).join(Users, Listing.user==Users.user_id)\
                .order_by(desc(Listing.created_at)).paginate(page_num, per_page=page_size, error_out=False)
        else:
            pagination = Listing.query.join(Users, Listing.user == Users.user_id) \
                .order_by(desc(Listing.created_at)).paginate(page_num, per_page=page_size, error_out=False)
        for each in pagination.items():
            temp = copy.deepcopy(result)
            temp['id'] = each.id
            temp['listing_type'] = each.listing_type
            temp['price'] = each.price
            temp['created_at'] = each.created_at
            temp['updated_at'] = each.updated_at
            temp['user']['id'] = each.user_id
            temp['user']['name'] = each.name
            temp['user']['created_at'] = each.created_at
            temp['user']['updated_at'] = each.updated_at

            listing.append(temp)
        return listing_return(True, listing)
    except BaseException as e:
        return listing_return(False, [])


def user_return(status, user_to_json):
    return {
        "result": status,
        "users": user_to_json
    }


def listing_return(status, listing_to_json):
    return {
        "result": status,
        "listing": listing_to_json
    }


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return str(e)
