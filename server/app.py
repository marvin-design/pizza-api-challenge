from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Register blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)