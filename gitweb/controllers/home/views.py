#coding=utf8
from  gitweb.controllers.home import home
from  flask import  redirect,render_template
from os.path import pardir
import os

@home.route("/")
def index():
    return render_template('index.html')
    #return os.getcwd()
@home.route('/banner')
def banner():
    return render_template('animation.html')

@home.route('/comment')
def comment():
    return  render_template('comments.html')

@home.route('/login')
def login():
   return render_template('login.html')

@home.route('/register')
def register():
    return render_template('register.html')

@home.route('/user')
def user():
    return  render_template('user.html')
