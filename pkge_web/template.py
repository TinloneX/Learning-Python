#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 快速打印
from util import p
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='admin':
        return render_template('signok.html', username=username)
    return render_template('signin.html', message='error', username=username)


if __name__ == '__main__':
    app.run()