from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TimeField, SelectField, IntegerField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange


class SignUpForm(FlaskForm):
    email = StringField('Email Address',  [
        validators.DataRequired(),
        validators.Email("Please provide a valid email address!")
    ])
    username = StringField('Username', validators=[
                           Length(min=5, max=100, message="Username must be between 5 to 100 characters"), DataRequired()])
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=5, max=100, message="Password must be between 5 to 100 characters"),
        EqualTo("confirmPassword", message="Passwords must match!")
    ])
    confirmPassword = PasswordField("Confirm Password")
    isSubscribe = BooleanField(
        "Check this box to receive newsletters from us")
    submit = SubmitField('Sign Up')


class OrderForm(FlaskForm):
    menu = SelectField(u'Menu', choices=[
        ('bun cha', 'Bun Cha'), ('pho', 'Pho'), ('dumpling', 'Dumpling')])
    numItem = IntegerField("Number of items", validators=[
        DataRequired(message="Please enter a number"),
        NumberRange(
            min=1, max=15, message="Enter a number between 1 to 15")
    ])
    date = DateField("Date of delivery", format='%m-%d-%Y',
                     validators=[DataRequired(message="Enter in the format mm-dd-YYYY")])
    note = StringField('Other note for your order')
    submit = SubmitField('Place Your Order')
