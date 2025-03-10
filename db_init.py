from models import db
from routes import app

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
