# coding: utf-8

from flask_wtf import Form
from app.models import Category
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Required, length, Regexp, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField


class LoginForm(Form):
    username = StringField(u'账号', validators=[Required(), length(6, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')


class RegistrationForm(Form):
    username = StringField(u'用户名', validators=[Required(), length(6, 18), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'只允许字母数字下划线')])
    password = PasswordField(u'密码', validators=[Required(), EqualTo('password2', message=u'密码错误提示1')])
    password2 = PasswordField(u'重复密码', validators=[Required()])
    real_name = StringField(u'昵称', validators=[Required()])
    registerkey = StringField(u'注册码', validators=[Required()])
    submit = SubmitField(u'注册')


class PostArticleForm(Form):
    title = StringField(u'标题', validators=[Required(), length(6, 64)])
    body = TextAreaField(u'内容')
    category_id = QuerySelectField(u'分类', query_factory=lambda: Category.query.all(), get_pk=lambda a: str(a.id), get_label=lambda a: a.name)
    submit = SubmitField(u'发布')


class PostCategoryForm(Form):
    name = StringField(u'分类名', validators=[Required(), length(6, 64)])
    submit = SubmitField(u'发布')
