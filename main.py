from flask import Flask, url_for, request, render_template, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'predpof_code_crusaders'


if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
