from flask import *
from models import *
from datetime import timedelta
from flask_login import LoginManager, login_user, logout_user, current_user
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ppo_pumpkin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pumpkin.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['UPLOAD_FOLDER'] = 'uploads/'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET'])
def home():
    return render_template('startpage.html')


@app.route('/registration', methods=['GET'])
def open_registration():
    return render_template('registration.html')


@app.route('/Auth/reg_check', methods=['POST'])
def registration():
    data = request.get_json()
    user = data['username']
    password = data['password']
    is_admin = int(data['admin'] == 'BigKoribskyTits')

    if User.query.filter_by(name=user).first():
        return make_response('This user already exists')

    to_db_user = User(name=user,
                      password=password,
                      is_admin=is_admin)
    db.session.add(to_db_user)
    db.session.commit()

    return make_response(f'Successfully registered;{is_admin}')


@app.route('/login', methods=['GET'])
def open_login():
    return render_template('login.html')


@app.route('/Auth/login_check', methods=['POST'])
def login():
    data = request.get_json()
    user = data['username']
    password = data['password']
    print('login', data)

    user = User.query.filter_by(name=user).first()
    if user and user.password == password:
        login_user(user)
        return make_response(f'Successfully logged in;{int(user.is_admin)}')
    else:
        return make_response('Wrong login or password')


@app.route('/user/main', methods=['GET'])
def user_main():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_main'))
    else:
        return redirect(url_for('home'))
    return render_template('user_main.html')


@app.route('/admin/main', methods=['GET'])
def admin_main():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            return redirect(url_for('user_main'))
    else:
        return redirect(url_for('home'))
    return render_template('admin_main.html')


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
