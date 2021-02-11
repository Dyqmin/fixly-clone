from flask import jsonify, request
from operator import itemgetter
import bcrypt
from src.db import db, User
from flask_restplus import Namespace, Resource, fields

users = Namespace('Users', description='Users namespace')
users_input = users.model('User', {
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'type': fields.String(required=True, description='User type id'),
})


@users.route('/users/<int:user_id>')
class Users(Resource):
    @users.doc('user')
    def get(self, user_id):
        '''Returns user`s data'''
        user_object = User.query.filter_by(id=user_id).first()
        if not user_object:
            users.abort(400, 'User with provided ID is not in database!')
        return jsonify(user_object.to_dict())


@users.route('/users/', methods=['GET', 'POST'])
class UsersList(Resource):
    @users.doc('users list')
    def get(self):
        """List all users"""
        return jsonify(users=[item.to_dict() for item in User.query.all()])

    @users.doc('user insert')
    @users.expect(users_input)
    def post(self):
        """Creates new user"""
        first_name, last_name, email, password, u_type = itemgetter(
            'first_name',
            'last_name',
            'email',
            'password',
            'type')(
            request.json)
        user_object = User.query.filter_by(email=email).first()
        if user_object:
            return jsonify(message='Email is already in database!'), 400
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, password=hashed_password.decode('utf-8'), user_type=u_type)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='User has been inserted!')
