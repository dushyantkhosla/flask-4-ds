from flask import render_template, url_for, flash, redirect, request

from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Dushyant Khosla',
        'title': 'Flask Web Apps 101',
        'content': 'Lorem Ipsum',
        'date_posted': 'Sep 4, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Data Science for Hackers',
        'content': 'Lorem Ipsum',
        'date_posted': 'Sep 2, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', payload=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='Flask4DS - About Us')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Flask4DS - Dash')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('home')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! You can now Log In.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('Login successful!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please try again.', 'danger')
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    user_image = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', title='My Account', image_file=user_image)
