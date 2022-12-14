from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()

    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                                email=form.email.data,
                                password_hash=form.password1.data)
        db.session.add(user_to_create)                        
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'There was an error: {error}')
    return render_template('register.html', form=form)
 