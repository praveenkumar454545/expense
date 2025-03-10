from flask import Flask
from extensions import db, login_manager  # ✅ Import from extensions.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/expense_tracker'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  

# ✅ Initialize Extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'app_routes.login'  # Ensure correct route name

# ✅ Import models after db is initialized
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Import routes AFTER app and db are set up
from routes import app_routes  
app.register_blueprint(app_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
