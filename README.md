# 🍕 Pizza Restaurant API

A RESTful API built with Flask, SQLAlchemy, and Flask-Migrate to manage pizza restaurants, their menus, and pizza associations.

---

## ✅ Features

- CRUD operations for Restaurants and Pizzas
- Add Pizzas to Restaurants with a join model (`RestaurantPizza`)
- SQLAlchemy ORM and Alembic migrations
- Input validations and JSON error responses
- Postman collection for quick testing

---

## ⚙️ Tech Stack

- Python 3.12+
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended (optional)
- Pipenv for environment management

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/marvin-design/pizza-restaurant-api.git
cd pizza-restaurant-api

2.Install Dependencies
pipenv install
pipenv shell

3. Set Environment Variables
export FLASK_APP=server.app:create_app
export FLASK_ENV=development

4. Initialize the Database
flask db init              # Run this only once
flask db migrate -m "Initial tables"
flask db upgrade

5. Seed the Database
python server/seed.py
```
🔌 API Endpoints
📍 Restaurants
Method	Endpoint	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<int:id>	Get single restaurant detail
DELETE	/restaurants/<int:id>	Delete a restaurant

🍕 Pizzas
Method	Endpoint	Description
GET	/pizzas	List all pizzas

🍽️ Restaurant Pizzas (Join Table)
Method	Endpoint	Description
POST	/restaurant_pizzas	Add a pizza to a restaurant

POST Request Body Example:

json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}
🧪 Example Requests
List all restaurants

bash
Copy
Edit
curl http://localhost:5000/restaurants
Create a pizza association

bash
Copy
Edit
curl -X POST http://localhost:5000/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{"price": 12, "pizza_id": 1, "restaurant_id": 2}'
🧱 Models
Restaurant
Field	Type	Notes
id	Integer	Primary Key
name	String	Required, max 50 chars
address	String	Required

Pizza
Field	Type	Notes
id	Integer	Primary Key
name	String	Required
ingredients	String	Required

RestaurantPizza (Join Table)
Field	Type	Notes
id	Integer	Primary Key
price	Integer	Must be between 1 and 30
restaurant_id	Integer	ForeignKey to Restaurant
pizza_id	Integer	ForeignKey to Pizza

🔬 Postman Testing
You can import the provided collection:
challenge-1-pizzas.postman_collection.json

Open Postman

Import collection

Use endpoints to test your API

🪪 License
MIT License
© 2025 Your Name

yaml
Copy
Edit

---

Would you like me to generate the `seed.py`, a working `create_app()` example, or sample controller/model files to go along with this `README`?











Tools





