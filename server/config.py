import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://dbuser1@localhost:5432/pizza_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False