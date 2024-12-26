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
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_main'))
        return redirect(url_for('user_main'))
    # create_base_db()
    return render_template('startpage.html')


@app.route('/registration', methods=['GET'])
def open_registration():
    if current_user.is_authenticated:
        return redirect(url_for('admin_main')) if current_user.is_admin else redirect(url_for('user_main'))
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

    login_user(to_db_user)
    return make_response(f'Successfully registered;{is_admin}')


@app.route('/login', methods=['GET'])
def open_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_main')) if current_user.is_admin else redirect(url_for('user_main'))
    return render_template('login.html')


@app.route('/Auth/login_check', methods=['POST'])
def login():
    data = request.get_json()
    user = data['username']
    password = data['password']

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
    requested_inventory_id = [take.id for take in Take.query.filter_by(user_id=current_user.id).all()]
    inventory = [[item.id, item.name, item.quantity, item.quality] for item in Inventory.query.filter(Inventory.id.in_(requested_inventory_id)).all()]
    return render_template('user_main.html', inventory=inventory)


@app.route('/admin/main', methods=['GET'])
def admin_main():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            return redirect(url_for('user_main'))
    else:
        return redirect(url_for('home'))
    return render_template('admin_main.html')


@app.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('open_login'))
    return redirect(url_for('home'))


def create_base_db():
    to_db_user = User(name='Bob',
                      password='BlaBla',
                      is_admin=0)
    db.session.add(to_db_user)
    to_db_user = User(name='Bob1',
                      password='BlaBla',
                      is_admin=0)
    db.session.add(to_db_user)
    to_db_user = User(name='BOB_ADMIN',
                      password='LoveAlice',
                      is_admin=1)
    db.session.add(to_db_user)
    to_db_inventory = Inventory(name='Сиськи Корибски малые',
                                quantity=50,
                                last_quantity=30,
                                quality='новые')
    db.session.add(to_db_inventory)
    to_db_inventory = Inventory(name='Сиськи Корибски большие',
                                quantity=10,
                                last_quantity=8,
                                quality='новые')
    db.session.add(to_db_inventory)
    to_db_inventory = Inventory(name='Сиськи Вольвача универсальные',
                                quantity=50,
                                last_quantity=40,
                                quality='новые')
    db.session.add(to_db_inventory)
    to_db_take = Take(user_id=1,
                      inventory_id=1,
                      quantity=20)
    db.session.add(to_db_take)
    to_db_take = Take(user_id=1,
                      inventory_id=2,
                      quantity=2)
    db.session.add(to_db_take)
    to_db_take = Take(user_id=2,
                      inventory_id=3,
                      quantity=10)
    db.session.add(to_db_take)
    db.session.commit()


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
