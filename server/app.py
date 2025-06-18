from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    Migrate(app, db)
    
    return app

app = create_app()