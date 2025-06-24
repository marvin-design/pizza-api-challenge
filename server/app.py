from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Note: Removed quotes around Config
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)  # This line is crucial
    
    # If you're using JWT
    # jwt.init_app(app)
    
    # Register blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)