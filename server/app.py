from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
   
    from server.models import db
    db.init_app(app)
    
   
    from server.models.restaurant import Restaurant
    from server.models.pizza import Pizza
    from server.models.restaurant_pizza import RestaurantPizza
    
    migrate = Migrate(app, db)
    
   
    with app.app_context():
        from server.controllers.restaurant_controller import restaurants_bp
        from server.controllers.pizza_controller import pizza_bp
        app.register_blueprint(restaurants_bp)
        app.register_blueprint(pizza_bp)
    
    return app