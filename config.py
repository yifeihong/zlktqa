#encoding: utf-8
import os

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlktqa'
USERNAME = 'root'
PASSWORD = '259925645'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

#邮箱配置信息
MAIL_SERVER ="smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME ="2849115967@qq.com"
MAIL_PASSWORD ="uqlbhymhdmrkddgg"
MAIL_DEFAULT_SENDER ="2849115967@qq.com"

SECRET_KEY = os.urandom(24)

SECRET_KE = "fafadgrawewga"