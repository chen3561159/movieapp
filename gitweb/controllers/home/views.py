#coding=utf8
from  gitweb.controllers.home import home
from  flask import  redirect,render_template

@home.route("/")
def index():
    return "<h1 style='color:red'>hello word</h1>"