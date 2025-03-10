from flask_login import UserMixin
from extensions import db  

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)  # ✅ Relationship

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # ✅ Added category field
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ✅ Foreign Key
