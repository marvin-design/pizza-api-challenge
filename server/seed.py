from server.app import app
from server.models import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Sample restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave")
        ]
        db.session.add_all(restaurants)

        # Sample pizzas
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
        ]
        db.session.add_all(pizzas)

        db.session.commit()

        # Sample restaurant_pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=12, pizza_id=2, restaurant_id=1)
        ]
        db.session.add_all(restaurant_pizzas)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()