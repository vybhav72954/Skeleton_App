from flask import Flask, render_template, redirect, url_for, flash
from forms import FirstForm, SecondForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = 'meof2ms0js4m2f2hczoj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskthapar.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_img = db.Column(db.String(20), nullable=False, default='default_photo.jpg')
    password = db.Column(db.String(60), nullable=False)
    information = db.relationship('Info', backref='Name', lazy=True)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_img}')"

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Hobby = db.Column(db.String(120), nullable=False)
    Job = db.Column(db.String(120), nullable=False, default="Unemployed")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.Hobby}','{self.Job}')"


posts = [
    {
        'Name': 'Vybhav',
        'Hobby': 'Footballer',
        'Job': 'Coder',
        'Quote': '!Hello World'
    },
    {
        'Name': 'Gaurav',
        'Hobby': 'Cleaner',
        'Job': 'Banker',
        'Quote': 'I haven\'t taken a bath yet'
    },
    {
        'Name': 'Saumya',
        'Hobby': 'Bully',
        'Job': 'Sales Head',
        'Quote': 'Hatttt'
    },

]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home', posts=posts)

@app.route('/about')
def About():
    return render_template('about.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FirstForm()
    if form.validate_on_submit():
        flash(f'Accont Created for {form.username.data}!', 'success')
        return redirect(url_for("index"))
    return render_template('register.html', title='Registration', form=form)

@app.route('/login')
def login():
    form = SecondForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
