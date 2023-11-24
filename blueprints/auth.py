import random
import string
from werkzeug.security import generate_password_hash
from models import EmailCaptchaModel, UserModel
from flask import Blueprint, render_template, jsonify,redirect,url_for
from exts import  mail,db
from flask_mail import Message
from flask import request
from .forms import RegisterForm
# /auth
bp = Blueprint("auth",__name__,url_prefix="/auth")
# 如果没有指定methods参数，默认就是get请求
@bp.route("/login")
def login():
    return "这是登录页面"

@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method =='GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # #表单验证:flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 4/6: 随机数组、宁母、数组和字母的组合
    source = string.digits*4
    captcha = random.sample(source,4)
    # print(captcha)
    captcha="".join(captcha)
    message = Message(subject="知了传课验证码", recipients=[email], body=f"您的验证码是{captcha}")
    mail.send(message)
    # memcached/redis
    # 用数据库表的方式存储
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    return jsonify({"code": 200,"message":"","data": None})

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试",recipients=["ygl2849115967@163.com"],body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"