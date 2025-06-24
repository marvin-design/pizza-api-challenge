from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize db with app
    db.init_app(app)
    
    # Import models (must be done after db initialization)
    from server.models.restaurant import Restaurant
    from server.models.pizza import Pizza
    from server.models.restaurant_pizza import RestaurantPizza
    
    # Create tables within application context
    with app.app_context():
        db.create_all()
    
    return app