from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'error')

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        dob = request.form['dob']
        gender = request.form['gender']
        phone = request.form['phone']
        address = request.form['address']
        pincode = request.form['pincode']
        state = request.form['state']

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            dob=dob,
            gender=gender,
            phone=phone,
            address=address,
            pincode=pincode,
            state=state
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Additional routes for other templates
@app.route('/aiinsightsjob')
def aiinsightsjob():
    return render_template('aiinsightsjob.html')

@app.route('/changepass')
def changepass():
    return render_template('changepass.html')

@app.route('/creativedgejob')
def creativedgejob():
    return render_template('creativedgejob.html')

@app.route('/cybershieldjob')
def cybershieldjob():
    return render_template('cybershieldjob.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/datacorpjob')
def datacorpjob():
    return render_template('datacorpjob.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/securetechjob')
def securetechjob():
    return render_template('securetechjob.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/techwavejob')
def techwavejob():
    return render_template('techwavejob.html')

@app.route('/webworksjob')
def webworksjob():
    return render_template('webworksjob.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)