from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)      
    
    db.init_app(app)
    migrate = Migrate(app, db) 
    
    # Updated import to match the corrected blueprint name
    from server.controllers.restaurant_controller import restaurants_bp  # Changed from restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    
    app.register_blueprint(restaurants_bp)  # Updated to match
    app.register_blueprint(pizza_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)