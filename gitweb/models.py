#coding=utf8
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime
db=SQLAlchemy()


class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)#名称
    pwd=db.Column(db.String(100))#密码
    email=db.Column(db.String(100),unique=True)#邮箱
    phone=db.Column(db.String(11),unique=True)#电话
    info=db.Column(db.Text)#个性简介
    face=db.Column(db.String(255),unique=True)#头像
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)#添加时间
    uuid=db.Column(db.String(255),unique=True)#唯一标识
    userlogs=db.relationship(
        'Userlog',
        backref='user'
    )
    comments=db.relationship(
        'Comment',
        backref='user'
    )


    def __repr__(self):
        return "<user %s>"%self.name


class Userlog(db.Model):
    __tablename__='userlog'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    ip=db.Column(db.String(100))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return  "<userlog %s>"%self.user.name

#标签
class Tag(db.Model):
    __tablename__='tag'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    addtime=db.Column(db.DateTime,default=datetime.now)
    movies=db.relationship(
        'Movie',
        backref='tag'
    )
    def __repr__(self):
        return  "<tag %s>"%self.name

class Movie(db.Model):
    __tablename__="movie"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),unique=True)#标题
    url=db.Column(db.String(255),unique=True)#url地址
    info=db.Column(db.Text)#简介
    logo=db.Column(db.String(255),unique=True)#封面
    star=db.Column(db.SmallInteger)#星级
    playnum=db.Column(db.BigInteger)#播放量
    commentnum=db.Column(db.BigInteger)#评论量
    tag_id=db.Column(db.Integer,db.ForeignKey('tag.id'))#所属标签
    area=db.Column(db.String(255))#上映地区
    release_time=db.Column(db.Date)#上映时间
    length=db.Column(db.String(255))#播放时间
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)#添加时间
    comments=db.relationship(
        'Comment',
        backref='movie'
    )

    def __repr__(self):
        return  "<Movie %s>"%self.title


class Preview(db.Model):
    __tablename__="preview"
    id=db.Column(db.Integer,primary_key=True)#编号
    title=db.Column(db.String(255),unique=True)#标题
    logo=db.Column(db.String(255),unique=True)#封面
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)#添加时间

    def __repr__(self):
        return "<Preview %s>"%self.title

class Comment(db.Model):
    __tablename__ = "preview"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Comment %s>"%self.Comment[0:20]


class Moviecol(db.Model):
    __tablename__="moviecol"
    id=db.Column(db.Integer,primary_key=True)#编号
    content=db.Column(db.Text)#内容
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'))#

