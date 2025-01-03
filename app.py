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

    taken_item = Take.query.filter_by(user_id=current_user.id).all()
    user_inventory = []
    for item in taken_item:
        product = Inventory.query.filter_by(id=item.id).first()
        fixes = FixRequest.query.filter_by(user_id=current_user.id, inventory_id=item.id).first()
        status = False
        if fixes:
            status = fixes.status
        user_inventory.append((product.id, product.name, item.quantity, product.quality, status))
    return render_template('user_main.html', inventory=user_inventory)


@app.route('/admin/main', methods=['GET'])
def admin_main():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            return redirect(url_for('user_main'))
    else:
        return redirect(url_for('home'))
    taken_item = Inventory.query.all()
    all_inventory = []
    for item in taken_item:
        all_inventory.append((item.id, item.name, item.quantity, item.last_quantity, item.quality))
    return render_template('admin_main.html', inventory=all_inventory)


@app.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('open_login'))
    return redirect(url_for('home'))


@app.route('/user/request_new_item', methods=['GET'])
def request_new_item():
    if current_user.is_authenticated:
        inventory = [[item.id, item.name, item.last_quantity, item.quality] for item in
                     Inventory.query.all()]
        return render_template('request_new_item.html', inventory=inventory)
    else:
        return redirect(url_for('home'))


@app.route('/admin/check_requests', methods=['GET'])
def check_requests():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            return redirect(url_for('user_main'))
    else:
        return redirect(url_for('home'))
    taken_item = FixRequest.query.filter(FixRequest.status == 'На рассмотрении').all()
    user_requests = []
    for ask in taken_item:
        user_requests.append((ask.id, User.query.filter(User.id == ask.user_id).first().name,
                              Inventory.query.filter(Inventory.id == ask.inventory_id).first().name,
                              Inventory.query.filter(Inventory.id == ask.inventory_id).first().quantity, ask.quality))
    return render_template('check_requests.html', user_requests=user_requests)


@app.route('/admin/purchases', methods=['GET'])
def purchases():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            return redirect(url_for('user_main'))
    else:
        return redirect(url_for('home'))

    taken_item = AdminRequest.query.all()
    admin_requests = []
    for item in taken_item:
        admin_requests.append((item.id, item.name, item.price, item.quantity, item.provider_name))
    return render_template('purchases.html', requests=admin_requests)


@app.route('/User/fix_item', methods=['POST'])
def fix_item():
    item_id = request.get_json()['item_id']
    item = Inventory.query.filter(Inventory.id == item_id).first()
    req = FixRequest()
    req.user_id = current_user.id
    req.inventory_id = item_id
    req.quality = item.quality
    req.status = 'На рассмотрении'
    db.session.add(req)
    db.session.commit()
    return make_response('The Best!')


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
