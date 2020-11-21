from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import SignUpForm, OrderForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
application = app
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('order.html', form=form)
