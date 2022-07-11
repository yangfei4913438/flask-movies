from flask import Blueprint, render_template, request

from lib.UserService import UserService
from model.user import User, db
from utils.dateHelper import get_current_time
from utils.jsonHelper import ops_render_err_json, ops_render_json

# 实例化蓝图，参数：蓝图名称，导入名称
custom_base = Blueprint('custom_base', __name__)


# 基础路由
@custom_base.route('/')
def hello():
    """
    基础路由
    """
    # 标题
    title = 'Home | 首页'

    # 欢迎语
    welcome = 'Hello World!'

    # 渲染页面
    return render_template('index.html', title=title, welcome=welcome)


# 注册页面
@custom_base.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # 标题
        title = 'Home | 注册'

        return render_template('register.html', title=title)

    # 不是get就是post
    req = request.values
    username = req['login_name'] if 'login_name' in req else ''
    password = req['login_pwd'] if 'login_pwd' in req else ''
    nick_name = req['nick_name'] if 'nick_name' in req else ''

    if username is None or len(username) < 5:
        return ops_render_err_json(msg='请输入正确的用户名'), 401

    user_info = User.query.filter_by(login_name=username).first()
    if user_info:
        return ops_render_err_json(msg='用户已存在，请换一个名字。'), 400

    if password is None or len(password) == 0:
        return ops_render_err_json(msg='您输入的用户名或密码有误，请重新输入。'), 401

    model_user = User()
    model_user.login_name = username
    model_user.nickname = nick_name
    model_user.login_salt = UserService.generator_salt(8)
    model_user.login_pwd = UserService.generator_pwd(password, model_user.login_salt)
    model_user.created_time = model_user.updated_time = get_current_time()

    db.session.add(model_user)
    db.session.commit()
    return ops_render_json(msg='注册成功!',
                           data={'username': username, 'password': password, '加密后:': model_user.login_pwd,
                                 'time': model_user.created_time}), 200


# 登陆页面
@custom_base.route('/login')
def login():
    # 标题
    title = 'Home | 登陆'

    return render_template('login.html', title=title)
