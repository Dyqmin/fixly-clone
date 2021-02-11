from flask import Blueprint, request, jsonify
from src.db import Order, db
from operator import itemgetter


orders = Blueprint('orders', __name__, template_folder='services')


@orders.route('/orders/<int:order_id>', methods=['GET', 'POST'])
def get_order(order_id):
    if request.method == 'GET':
        user_object = Order.query.filter_by(id=order_id).first()
        if not user_object:
            return jsonify(message='Order with provided ID is not in database!'), 400
        return jsonify(user_object.to_dict())


@orders.route('/orders/', methods=['POST', 'GET'])
def create_order():
    if request.method == 'POST':
        description, client_id, order_type_id = itemgetter(
            'description',
            'client_id',
            'order_type_id')(
            request.values)
        if not description or not client_id or not order_type_id:
            return jsonify(message='Some parameters are missing!'), 400
        new_order = Order(description=description, client_id=client_id, order_type_id=order_type_id)
        db.session.add(new_order)
        db.session.commit()
        return jsonify(message='Order has been inserted!')
    if request.method == 'GET':
        return jsonify(orders=[item.to_dict() for item in Order.query.all()])
