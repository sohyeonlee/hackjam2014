from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import User, RegistrationForm, SigninForm
from database import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '$\xf8\x81\xb2[J_l\x0c\x18\x86^p\xc9\xba\xb3\x88_\x03\xc8\x9dz\xf4/'
db = SQLAlchemy(app)


@app.route('/')
def index():
    print(User.query.first())
    return render_template('index.html')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('index.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('index'))
                 
  elif request.method == 'GET':
    return render_template('login.html', form=form)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        print("i m here")
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)  

      
if __name__ == '__main__':
     app.run(debug=True)
