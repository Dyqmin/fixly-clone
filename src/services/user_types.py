from flask import Blueprint, jsonify
from src.db import UserType

user_types = Blueprint('user_types', __name__, template_folder='services')


@user_types.route('/user-types/', methods=['GET'])
def get_user_types():
    return jsonify(user_types=[item.to_dict() for item in UserType.query.all()])
