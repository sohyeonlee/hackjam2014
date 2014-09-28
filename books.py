from flask import Flask, render_template, session, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import User, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '$\xf8\x81\xb2[J_l\x0c\x18\x86^p\xc9\xba\xb3\x88_\x03\xc8\x9dz\xf4/'
db = SQLAlchemy(app)
engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

@app.route('/')
def index():
    return render_template('index.html')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('register'))
    return render_template('login.html', error=error)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        print("i m here")
        db_session.add(user)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)  
      
if __name__ == '__main__':
     app.run(debug=True)
