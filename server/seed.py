from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_database():
    with app.app_context():
        try:
            # Clear existing data
            db.session.query(RestaurantPizza).delete()
            db.session.query(Restaurant).delete()
            db.session.query(Pizza).delete()
            
            # Create restaurants
            restaurants = [
                Restaurant(name="Pizza Palace", address="123 Main St"),
                Restaurant(name="Italian Bistro", address="456 Oak Ave")
            ]
            db.session.add_all(restaurants)
            
            # Create pizzas
            pizzas = [
                Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
                Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
            ]
            db.session.add_all(pizzas)
            
            db.session.commit()
            
            # Create associations
            restaurant_pizzas = [
                RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
                RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
                RestaurantPizza(price=11, pizza_id=1, restaurant_id=2)
            ]
            db.session.add_all(restaurant_pizzas)
            db.session.commit()
            
            print("✅ Database seeded successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error seeding database: {str(e)}")

if __name__ == '__main__':
    seed_database()