from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin


migrate = Migrate()
db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    password = db.Column(db.Text, nullable=False)


class UserType(db.Model, SerializerMixin):
    __tablename__ = 'user_types'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Integer(), nullable=False)


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer(), primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_type_id = db.Column(db.Integer, db.ForeignKey('order_types.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)


class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer(), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    contractor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)


class OrderType(db.Model, SerializerMixin):
    __tablename__ = 'order_types'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Integer(), nullable=False)
