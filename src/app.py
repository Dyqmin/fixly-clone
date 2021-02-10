from flask import Flask, request, jsonify, Response, abort
from db import db, migrate, User, UserType
import os
from operator import itemgetter
import bcrypt

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/test/', methods=['GET'])
    def test():
        password = itemgetter('password')(request.values)
        pwhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return jsonify({"password": pwhash.decode("utf-8")})

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user_object = User.query.filter_by(id=user_id).first()
        if not user_object:
            return jsonify(message='User with provided ID is not in database!'), 400
        return jsonify(user_object.to_dict())

    @app.route('/user-types/', methods=['GET'])
    def get_user_types():
        return jsonify(user_types=[item.to_dict() for item in UserType.query.all()])

    @app.route('/users/', methods=['GET', 'POST'])
    def create_user():
        if request.method == 'POST':
            first_name, last_name, email, password, type = itemgetter(
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
                            email=email, password=hashed_password.decode('utf-8'), user_type=type)
            db.session.add(new_user)
            db.session.commit()
            return jsonify(message='User has been inserted!')

        if request.method == 'GET':
            return jsonify(users=[item.to_dict() for item in User.query.all()])

    @app.route('/login/', methods=['GET', 'POST'])
    def login():
        email, password = itemgetter('email', 'password')(
            request.values)
        user_object = User.query.filter_by(email=email).first()
        if not user_object or not bcrypt.checkpw(
                password.encode('utf-8'),
                user_object.to_dict()['password'].encode('utf-8')):
            return jsonify(message='Wrong user or password!'), 400
        return 'dziala'

    return app


if __name__ == "__main__":
    create_app()
