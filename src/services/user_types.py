from flask import jsonify
from flask_restplus import Namespace, Resource
from src.db import UserType


user_types = Namespace('User Types', description='User Types namespace')


@user_types.route('/user-types/')
class UserTypes(Resource):
    @user_types.doc('user types')
    def get(self):
        """List all types of user"""
        return jsonify(user_types=[item.to_dict() for item in UserType.query.all()])
