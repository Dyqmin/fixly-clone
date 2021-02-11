from flask_restplus import Api
from flask import Blueprint
from src.services import users, user_types, login, order_types, orders, offers


def init_api(app):
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
