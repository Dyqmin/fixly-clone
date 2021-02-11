from flask import Flask, request, jsonify, Response, abort
from db import db, migrate, User, UserType
import os
from src.services import register, users, user_types, login


POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(register.register)
    app.register_blueprint(users.users)
    app.register_blueprint(user_types.user_types)
    app.register_blueprint(login.login)

    return app


if __name__ == "__main__":
    create_app()
