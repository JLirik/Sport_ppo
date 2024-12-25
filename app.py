from flask import *
from models import *
from datetime import timedelta
from flask_login import LoginManager, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ppo_pumpkin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pumpkin.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['UPLOAD_FOLDER'] = 'uploads/'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    pass


@app.route('/registration', methods=['GET'])
def open_registration():
    return render_template('register.html')


@app.route('/Auth/reg_check', methods=['POST'])
def registration():
    data = request.get_json()
    user = data['username']
    password = data['password']
    code = data['admin']
    print(1, User.query.filter_by(name=user).first())
    if User.query.filter_by(name=user).first():
        return make_response('This user already exists')

    print(user, password)
    to_db_user = User(name=user,
                      password=password,
                      is_admin=code == 'BigKoribskyTits')
    db.session.add(to_db_user)
    db.session.commit()
    if code == 'BigKoribskyTits':
        # admin
        pass
    else:
        # user
        pass


@app.route('/enter', methods=['GET'])
def open_enter():
    return render_template('enter.html')


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
