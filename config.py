import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/expense_tracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
