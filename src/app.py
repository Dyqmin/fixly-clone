from flask import Flask, Blueprint
from src.db import db, migrate
import os
from src.services import users, user_types, login, order_types, orders, offers
from flask_restplus import Api, Resource


POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(version='1.0', title='Fixly clone',
              description='WIT Project for Python basics course')
    api.init_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(login.login)
    api.add_namespace(users.users)
    api.add_namespace(order_types.order_types)
    api.add_namespace(user_types.user_types)
    api.add_namespace(orders.orders)
    api.add_namespace(offers.offers)
    app.register_blueprint(blueprint)

    return app


if __name__ == "__main__":
    create_app()
