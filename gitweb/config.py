#coding=utf8
class Config(object):
    DEBUG=True#注意要大写
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123@127.0.0.1/movieapp'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
