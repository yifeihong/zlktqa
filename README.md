1. 安装所需库，这个库比较特殊，其他库自行安装解决
``pip install flask-migrate``

2. 迁移三部曲(用来迁移数据库)

``flask db init ``

``flask db migrate``

``flask db upgrade``

最后会生成一个migrations文件,并且数据库中会多两张表

修改html路径，

发送验证码：
1. 安装flask库:
    ``pip install flask-mail``    
2. 创建flask-mail 然后在config中配置邮箱信息，在exts中创建，app中引用并初始化，然后在auth.py中创建视图函数
3. 先创建/mail/test，并成功测试邮箱。然后创建/captcha/email视图函数实现发送邮箱的功能，但是还是有欠缺。
4. 将验证码存储到数据库(更改models),然后再走一下三部曲,ajax返回json格式字符串
    ![img.png](img.png)
    ![img_1.png](img_1.png)
5. 后端已经写好，用ajax补充前端:js后执行问题\
6. 补充验证码的倒计时功能

表单验证功能：
1. 安装库：
``pip install flask-wtf``
2. 创建forms.py，验证邮箱以及验证码
3. 安装包：
``pip install email_validator``