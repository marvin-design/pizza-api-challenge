from server import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    
    
    restaurant_pizzas = db.relationship(
        'RestaurantPizza', 
        back_populates='restaurant',
        lazy=True
    )