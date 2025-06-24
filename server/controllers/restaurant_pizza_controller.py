# server/controllers/restaurant_pizza_controller.py
from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    
    # Verify pizza and restaurant exist
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    if not pizza or not restaurant:
        return jsonify({'errors': ['Pizza or Restaurant not found']}), 400
    
    db.session.add(restaurant_pizza)
    db.session.commit()
    
    return jsonify({
        'id': restaurant_pizza.id,
        'price': restaurant_pizza.price,
        'pizza_id': restaurant_pizza.pizza_id,
        'restaurant_id': restaurant_pizza.restaurant_id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201