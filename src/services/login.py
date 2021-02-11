from flask import Blueprint, request, jsonify
from operator import itemgetter
import bcrypt
from src.db import User

login = Blueprint('login', __name__, template_folder='services')


@login.route('/login/', methods=['GET'])
def get_login():
    email, password = itemgetter('email', 'password')(
        request.values)
    user_object = User.query.filter_by(email=email).first()
    if not user_object or not bcrypt.checkpw(
            password.encode('utf-8'),
            user_object.to_dict()['password'].encode('utf-8')):
        return jsonify(message='Wrong user or password!'), 400
    return 'dziala'
