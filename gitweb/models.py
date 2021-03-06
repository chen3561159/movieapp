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
    moviecols=db.relationship(
        'Moviecol',
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
    moviecols=db.relationship(
        'Moviecol',
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
#电影评论
class Comment(db.Model):
    __tablename__ = "comment"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return "<Comment %s>"%self.Comment[0:20]

#电影收藏
class Moviecol(db.Model):
    __tablename__="moviecol"
    id=db.Column(db.Integer,primary_key=True)#编号
    content=db.Column(db.Text)#内容
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'))#
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return  "<moviecol %s>" %self.id


auths=db.Table('role_auth',
    db.Column('auth_id',db.Integer,db.ForeignKey('auth.id')),
    db.Column('role_id',db.Integer,db.ForeignKey('role.id'))
)


class Auth(db.Model):
    __tablename__='auth'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    url=db.Column(db.String(255),unique=True)
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

    def __repr__(self):
        return  "<auth %s>"%self.name

class Role(db.Model):
    __tablename__="role"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    auths=db.Column(db.String(600))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)
    auths=db.relationship(
        'Auth',
        secondary=auths,
        backref=db.backref('roles',lazy='dynamic')
    )
    admins=db.relationship(
        'Admin',
        backref='role'
    )
    def __repr__(self):
        return  "<Role %s>"%self.name


class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)#管理员帐号
    pwd=db.Column(db.String(100))#管理员密码
    is_super=db.Column(db.SmallInteger)#是否为超级管理员
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)
    adminlogs=db.relationship(
        'Adminlog',
        backref='admin'
    )#该管理元的所有登陆日志
    oplogs=db.relationship(
        'Oplog',
        backref='admin'
    )
    def __repr__(self):
        return  "<admin %s>"%self.name

class Adminlog(db.Model):
    __tablename__="adminlog"
    id=db.Column(db.Integer,primary_key=True)
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id'))#所属管理员
    ip=db.Column(db.String(100))#登陆IP
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)#添加时间

    def __repr__(self):
        return "<adminlog %s>"%self.id

#操作日志
class Oplog(db.Model):
    __tablename__='oplog'
    id=db.Column(db.Integer,primary_key=True)#编号
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.id'))
    ip=db.Column(db.String(100))#登陆IP
    reason=db.Column(db.String(600))#操作原因
    addtime=db.Column(db.DateTime,index=True,default=datetime.now)

