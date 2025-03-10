from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models import User, Expense
from forms import LoginForm, RegisterForm

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    return redirect(url_for('app_routes.login' if User.query.first() else 'app_routes.register'))

@app_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('app_routes.login'))
        
        new_user = User(name=form.name.data, email=form.email.data, password=form.password.data)  # No hashing
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('app_routes.dashboard'))
    
    return render_template('register.html', form=form)

@app_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('app_routes.dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app_routes.route('/dashboard')
@login_required
def dashboard():
    expenses = Expense.query.filter_by(user_id=current_user.id).all() or []
    return render_template('dashboard.html', expenses=expenses)

@app_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('app_routes.login'))

@app_routes.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        name, amount, date = request.form.get('name'), request.form.get('amount'), request.form.get('date')
        if not all([name, amount, date]):
            flash("All fields are required!", "danger")
            return redirect(url_for('app_routes.dashboard'))
        
        db.session.add(Expense(name=name, amount=amount, date=date, user_id=current_user.id))
        db.session.commit()
        flash("Expense added successfully!", "success")
        return redirect(url_for('app_routes.dashboard'))
    
    return render_template('add_expense.html')

@app_routes.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.name, expense.amount, expense.date = request.form['name'], request.form['amount'], request.form['date']
        db.session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('app_routes.dashboard'))
    
    return render_template('edit_expense.html', expense=expense)

@app_routes.route('/delete_expense/<int:id>', methods=['POST'])
@login_required
def delete_expense(id):
    db.session.delete(Expense.query.get_or_404(id))
    db.session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('app_routes.dashboard'))
