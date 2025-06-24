import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://pizza_user:new_secure_password@localhost/pizza_restaurant'
    SQLALCHEMY_TRACK_MODIFICATIONS = False