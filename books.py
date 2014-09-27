from flask import Flask, render_template, session, redirect, url_for
from flask.ext.login import LoginManager, current_user
from flask.ext.login import login_user, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.setup_app(app)
#login_manager.login_view = 'login'

@app.route('/')
def index():
    if 'username' in session:
        return "welcome"
    return "Please login"
    
#
# @app.route('/login', methods=['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         return "login"
#     else:
#         return "signupform"

@login_manager.user_loader
def load_user(user_id):
    """Flask-Login hook to load a User instance from ID."""
    return db.session.query(User).get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('appointment_list'))
        form = LoginForm(request.form)
        error = None

    if request.method == 'POST' and form.validate():
        email = form.username.data.lower().strip()
        password = form.password.data.lower().strip()
        user, authenticated = \
        User.authenticate(db.session.query, email,password)
    if authenticated:
        login_user(user)
        return redirect(url_for('appointment_list'))
    else:
        error = 'Incorrect username or password.'
        # return render_template('user/login.html', form=form, error=error)
        return "error"

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
    
# set the secret key.  keep this really secret:
app.secret_key = '$\xf8\x81\xb2[J_l\x0c\x18\x86^p\xc9\xba\xb3\x88_\x03\xc8\x9dz\xf4/'