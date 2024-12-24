import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ppo_pumpkin'


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
