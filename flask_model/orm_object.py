from . import db


class Users(db.Model):
    __tablename = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    service = db.relationship('Service', backref='user', lazy='dynamic')

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Listing(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    price = db.Column(db.Integer)
    listing_type = db.Column(db.Text)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'price': self.price,
            'listing_type': self.listing_type,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }