from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, EmailField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")

class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Shopping', 'Shopping'), ('Bills', 'Bills'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Add Expense')

class FilterForm(FlaskForm):
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d')
    category = SelectField('Category', choices=[('', 'All'), ('Food', 'Food'), ('Transport', 'Transport'), ('Shopping', 'Shopping'), ('Bills', 'Bills'), ('Other', 'Other')])
    submit = SubmitField('Filter')
