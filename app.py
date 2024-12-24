from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ppo_pumpkin'


@app.route('/')
def home():
    pass


@app.route('/registration', methods=['GET'])
def open_registration():
    return render_template('register.html')


@app.route('/registration', methods=['POST'])
def regisration():
    user = request.form['username']
    password = request.form['password']
    code = request.form['admin-code']
    if not user or not password:
        flash('Введены не все данные')
        return redirect('/registration')
    print(user, password)
    if code:
        pass
    else:
        pass


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
