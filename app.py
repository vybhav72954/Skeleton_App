from flask import Flask, render_template, redirect, url_for, flash
from forms import FirstForm, SecondForm

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'meof2ms0js4m2f2hczoj'
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
    return render_template('index.html', title='Home')

@app.route('/about')
def About():
    return render_template('about.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FirstForm()
    if form.validate_on_submit():
        flash(f'Accont Created for {form.username.data}!', 'success')
        return redirect(url_for("index"))
    return render_template('register.html', title='Bhar Bhai', form=form)

@app.route('/login')
def login():
    form = SecondForm()
    return render_template('login.html', title='Bta Bhai', form=form)

if __name__ == '__main__':
    app.run(debug=True)
