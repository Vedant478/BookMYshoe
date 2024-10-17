from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bookmyshow'
app.config['SECRET_KEY'] = 'your_secret_key'  
db = SQLAlchemy(app)

# Define your SignUp model
class SignUp(db.Model):
    __tablename__ = 'sign_up'
    id = db.Column(db.Integer, primary_key=True)  # Make sure the id column is here
    name = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user already exists
        existing_user = SignUp.query.filter((SignUp.name == name) | (SignUp.email == email)).first()
        if existing_user:
            flash('Username or email already exists! Please choose a different one.')
            return redirect(url_for('signup'))
        
        # Create a new user
        new_user = SignUp(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Sign up successful! You can now log in.')
        return redirect(url_for('signup'))

    return render_template('signup.html')

# Route for the home page
@app.route('/')
def home():
    return redirect(url_for('signup'))

if __name__ == '__main__':
    with app.app_context():  # Use application context to create the tables
        db.create_all()  # Create the database tables
    app.run(debug=True)
