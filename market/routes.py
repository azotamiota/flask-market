from market import app
from flask import render_template
from market.models import Item, User
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()

    return render_template('market.html', items=items)

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                                email=form.email.data,
                                password=form.password1.data)
                                
    return render_template('register.html', form=form)
