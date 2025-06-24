from flask import Flask
from flask_migrate import Migrate
from server.extensions import db  

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
   
    db.init_app(app)
    migrate = Migrate(app, db)
    
   
    with app.app_context():
        from server.models import Restaurant, Pizza, RestaurantPizza
        
      
        from server.controllers.restaurant_controller import restaurants_bp
        from server.controllers.pizza_controller import pizza_bp
        app.register_blueprint(restaurants_bp)
        app.register_blueprint(pizza_bp)
    
    return app

app = create_app()