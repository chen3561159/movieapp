#coding=utf8
from flask import Flask,render_template
from gitweb.config import Config
from gitweb.controllers.admin import admin as admin_blueprint
from gitweb.controllers.home import home as home_blueprint
from models import db
app=Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix='/admin')

db.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404
