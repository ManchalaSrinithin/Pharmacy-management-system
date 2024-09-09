from flask import Blueprint, request, jsonify
from app import db
from app.models import Product

bp = Blueprint('routes', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'quantity': product.quantity,
        'price': product.price
    } for product in products])

@bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        quantity=data['quantity'],
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({
        'id': new_product.id,
        'name': new_product.name,
        'quantity': new_product.quantity,
        'price': new_product.price
    }), 201
