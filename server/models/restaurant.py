from server import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # Added nullable=False
    address = db.Column(db.String(100), nullable=False)
    
    # Improved relationship configuration
    pizzas = db.relationship(
        'Pizza',
        secondary='restaurant_pizzas',  # Assuming you have an association table
        back_populates='restaurants',  # More explicit than backref
        viewonly=True  # If this is just for querying
    )
    
    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',  # Requires corresponding back_populates in RestaurantPizza
        cascade='all, delete-orphan',
        lazy='dynamic'  # Optional: for large datasets
    )
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'