from server import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    __table_args__={'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    
    restaurant_pizzas = db.relationship('RestaurantPizza',  backref='pizza', cascade='all, delete-orphan')