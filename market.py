import email
from email.policy import default
from enum import unique
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'be81e9c0c617dbb20f7ce184'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    email_address = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    budget = db.Column(db.String(),nullable=False,default=1000)
    #This is the link between the User and the Items that he/she owns 
    items = db.relationship('Item',backref='owned_user',lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'{self.name}'


@app.route('/') 
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register',methods=['GET','POST'])
def  register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address = form.email_address.data,
                              password_hash = form.password1.data)
        db.session.add(user_to_create )
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # If no errors from form 
        for err_msg in form.errors.values():
            print(f'An eeror occured: {err_msg}') 
    return render_template('register.html',form = form)


if __name__ == '__main__':
    app.run(debug=True)