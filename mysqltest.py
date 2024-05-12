from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__)

HOSTNAME="127.0.0.1"
#mgsql监听的端口号，默认3306
PORT = 3306
#连mgsql的用户名，读者用自己设置的
USERNAME = "liu"
#连msql的密码，读者用自己的
PASSWORD = "12345678"
#mgsql上创建的数据库名称
DATABASE = "flaskt1"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)

class AuthorModel(db.Model):
    __tablename__= "author"
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    articals = db.relationship('ArticalModel')

class ArticalModel(db.Model):
    __tablename__= "artical"
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    articalname = db.Column(db.String(100),nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    #author = db.relationship(AuthorModel,backref="questions")

with app.app_context():
    db.create_all()

# 在app.config中设置好连接数据库的信息，
# 然后使用sqlalchemy(app)创健一个db对象
# sqlalchemg会自动读取app.config中连接数据库的信息

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text('select 1'))
        print(rs.fetchone()) #(1,)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/add')
def add():
    au1 = ArticalModel(articalname='arti1',author_id=1)
    au2 = ArticalModel(articalname='arti2',author_id=1)
    db.session.add_all([au1, au2])
    db.session.commit()
    return 'add seccused'

@app.route('/cha')
def cha():
    au = AuthorModel.query.get(1)
    print(au.username)
    ars = au.articals
    for ar in ars:
        print(ar.articalname)
    return 'add seccused'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
