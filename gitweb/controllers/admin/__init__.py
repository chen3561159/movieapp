#coding=utf8
from flask import Blueprint
from os.path import pardir
import os
admin=Blueprint(
    'admin',
    __name__,
    template_folder=os.path.join(os.getcwd(), 'gitweb', 'templates', 'admin')
)
import gitweb.controllers.home.views