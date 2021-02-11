from flask import request, jsonify
from src.db import Order, db
from operator import itemgetter
from flask_restplus import Namespace, Resource, fields


orders = Namespace('Orders', description='Orders namespace')
orders_input = orders.model('Orders', {
    'client_id': fields.String(required=True, description='User id', example='7'),
    'order_type_id': fields.String(required=True, description='Type of order', example='1'),
    'description': fields.String(required=True, description='Description of an order',
                                 example='My computer stopped working')
})


@orders.route('/orders/<int:order_id>')
class OrderData(Resource):
    @orders.doc('order')
    def get(self, order_id):
        """Return order data"""
        order_data = Order.query.filter_by(id=order_id).first()
        if not order_data:
            orders.abort(400, 'Order with provided ID is not in database!')
        return jsonify(order_data.to_dict())


@orders.route('/orders/')
class Orders(Resource):
    @orders.doc('order create')
    @orders.expect(orders_input)
    def post(self):
        """Create new order"""
        description, client_id, order_type_id = itemgetter(
            'description',
            'client_id',
            'order_type_id')(
            request.json)
        if not description or not client_id or not order_type_id:
            return jsonify(message='Some parameters are missing!'), 400
        new_order = Order(description=description, client_id=client_id, order_type_id=order_type_id)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(message='Order has been inserted!')

    def get(self):
        """List all orders"""
        return jsonify(orders=[item.to_dict() for item in Order.query.all()])
