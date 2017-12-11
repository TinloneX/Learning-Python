#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/sina', methods=['GET'])
def sina():
    # 返回静态网页内容
    with open('../files/sinal.html', 'rb') as f:
        return str(f.read(), encoding='utf-8').encode('utf-8')


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return '<h3>Hello,admin</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
