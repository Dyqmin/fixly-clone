from flask import Blueprint, request, jsonify
from operator import itemgetter
import bcrypt
from src.db import User
from flask_restplus import Namespace, Resource, fields


login = Namespace('Auth', description='Auth namespace')
login_input = login.model('Login', {
    'email': fields.String(required=True, description='User email', example='test3@test.pl'),
    'password': fields.String(required=True, description='User password', example='test')
})


@login.route('/login')
class Login(Resource):
    @login.doc('login')
    @login.expect(login_input)
    def post(self):
        """Logins into an app"""
        email, password = itemgetter('email', 'password')(
            request.json)
        user_object = User.query.filter_by(email=email).first()
        if not user_object or not bcrypt.checkpw(
                password.encode('utf-8'),
                user_object.to_dict()['password'].encode('utf-8')):
            return jsonify(message='Wrong user or password!'), 400
        return jsonify(message='Successful login!')
