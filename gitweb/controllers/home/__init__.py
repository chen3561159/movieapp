#coding=utf8
from flask import Blueprint
from os.path import pardir
import os

home=Blueprint(
    'home',
    __name__,
    template_folder=os.path.join(os.getcwd(),'gitweb','templates','home')
    #template_folder是指定该蓝图下的模板从哪里开始查找
    #template_folder的路径一定要写对否则它会按默认的从templates开始查找模板
)
import gitweb.controllers.home.views