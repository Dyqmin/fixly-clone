from flask import Blueprint, jsonify
from src.db import OrderType

order_types = Blueprint('order_types', __name__, template_folder='services')


@order_types.route('/order-types/', methods=['GET'])
def get_order_types():
    return jsonify(order_types=[item.to_dict() for item in OrderType.query.all()])
