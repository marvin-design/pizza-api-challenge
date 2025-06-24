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

### 2.Install Dependencies
pipenv install
pipenv shell

### 3. Set Environment Variables
export FLASK_APP=server.app:create_app
export FLASK_ENV=development


