# coding: utf-8

from __future__ import unicode_literals

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db, login_manager


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'create_time': datetime.strftime(self.create_time, '%Y-%m-%dT%H:%M:%S'),
            'category': self.category.name,
            'category_id': self.category_id,
            'user': self.user.real_name
        }


class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='category')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            }


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='user')
    comments = db.relationship('Comment', backref='comment_user')

    @property
    def password(self):
        raise AttributeError(u'密码属性不正确')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True, default=None)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    def to_dict(self):
        return {
            'comment_id': self.id,
            'content': self.content,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': self.user_id,
            'article_id': self.article_id
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
