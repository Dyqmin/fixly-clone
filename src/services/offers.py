from flask import jsonify, request
from flask_restplus import Namespace, Resource, fields
from operator import itemgetter
from src.db import Offer, db


offers = Namespace('Offers', description='Offers namespace')
offers_input = offers.model('Orders', {
    'order_id': fields.String(required=True, description='Id of order that exists in database', example='2'),
    'contractor_id': fields.String(required=True, description='User id who is a contractor', example='8'),
    'price': fields.String(required=True, description='Price of an offer', example='500')
})


@offers.route('/offers/')
class OffersList(Resource):
    @offers.doc('offers')
    def get(self):
        """List all offers"""
        return jsonify(user_types=[item.to_dict() for item in Offer.query.all()])

    @offers.doc('offer create')
    @offers.expect(offers_input)
    def post(self):
        """Create new order"""
        order_id, contractor_id, price = itemgetter(
            'order_id',
            'contractor_id',
            'price')(
            request.json)
        if not order_id or not contractor_id or not price:
            return jsonify(message='Some parameters are missing!'), 400
        new_offer = Offer(order_id=order_id, contractor_id=contractor_id, price=price)
        db.session.add(new_offer)
        db.session.commit()
        return jsonify(message='Offer has been inserted!')
