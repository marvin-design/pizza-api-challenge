# server/models/restaurant_pizza.py
from server import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    def __init__(self, price, pizza_id, restaurant_id):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id