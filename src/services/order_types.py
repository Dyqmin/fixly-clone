from flask import jsonify
from flask_restplus import Namespace, Resource
from src.db import OrderType


order_types = Namespace('Order Types', description='Order Types namespace')


@order_types.route('/order-types/')
class OrderTypes(Resource):
    @order_types.doc('order types')
    def get(self):
        """List all types of order"""
        return jsonify(order_types=[item.to_dict() for item in OrderType.query.all()])
