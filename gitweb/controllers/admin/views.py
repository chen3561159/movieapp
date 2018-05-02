#coding=utf8
from  gitweb.controllers.admin import admin
from  flask import  redirect,render_template

@admin.route("/")
def index():
    return "<h1 style='color:red'>hello word</h1>"