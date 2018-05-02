#coding=utf8
from flask import Blueprint
from os.path import pardir
import os
admin=Blueprint(
    'admin',
    __name__,
    template_folder=os.path.join(pardir,'..','templates','admin'),
    static_folder=os.path.join(pardir,'..','static'),

)
import gitweb.controllers.home.views