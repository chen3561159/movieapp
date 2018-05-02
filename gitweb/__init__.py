#coding=utf8
from flask import Flask
from gitweb.config import Config
from gitweb.controllers.admin import admin as admin_blueprint
from gitweb.controllers.home import home as home_blueprint
from models import db
app=Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin_blueprint,url_prefix='/admin')
app.register_blueprint(home_blueprint)
db.init_app(app)
