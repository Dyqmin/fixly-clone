from flask import Blueprint, jsonify, request
from operator import itemgetter
import bcrypt
from src.db import db, User

users = Blueprint('users', __name__, template_folder='services')


@users.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_object = User.query.filter_by(id=user_id).first()
    if not user_object:
        return jsonify(message='User with provided ID is not in database!'), 400
    return jsonify(user_object.to_dict())


@users.route('/users/', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        first_name, last_name, email, password, u_type = itemgetter(
            'first_name',
            'last_name',
            'email',
            'password',
            'type')(
            request.values)
        user_object = User.query.filter_by(email=email).first()
        if user_object:
            return jsonify(message='Email is already in database!'), 400
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, password=hashed_password.decode('utf-8'), user_type=u_type)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='User has been inserted!')

    if request.method == 'GET':
        return jsonify(users=[item.to_dict() for item in User.query.all()])
