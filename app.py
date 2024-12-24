from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ppo_pumpkin'


@app.route('/')
def home():
    pass


@app.route('/registration', methods=['GET'])
def open_registration():
    print(8)
    return render_template('register.html')


@app.route('/registration', methods=['POST'])
def regisration():
    data = request.get_json()
    print(data)
    user = data['username']
    password = data['password']
    code = data['admin']
    if not user or not password:
        flash('Введены не все данные')
        return redirect('/registration')

    # Проверить на наличие почты в БД - надо функцию

    print(user, password)
    if code:
        # admin
        pass
    else:
        # user
        pass


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
