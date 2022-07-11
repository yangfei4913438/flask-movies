from flask import Blueprint, make_response, redirect, request

# from application import app
from lib.UserService import UserService
from lib.urlManager import UrlManger
from model.user import User, db
from utils.dateHelper import get_current_time
from utils.helper import auth_render, ops_render_err_json, ops_render_json

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

    # from flask import session 登陆成功后，自动存储到session中（不推荐，推荐使用插件，存储到redis等内存数据库中）
    # app.logger.info(session['uid'])

    # 渲染页面
    return auth_render('index.html', title=title, welcome=welcome)


# 注册页面
@custom_base.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # 标题
        title = 'Home | 注册'

        return auth_render('register.html', title=title)

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
@custom_base.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 标题
        title = 'Home | 登陆'

        return auth_render('login.html', title=title)

    # 不是get就是post
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 5:
        return ops_render_err_json(msg='请输入正确的用户名'), 401

    if login_pwd is None or len(login_pwd) == 0:
        return ops_render_err_json(msg='您输入的用户名或密码有误，请重新输入。'), 401

    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        return ops_render_err_json(msg='请输入正确的用户名或密码'), 401

    if user_info.login_pwd != UserService.generator_pwd(login_pwd, user_info.login_salt):
        return ops_render_err_json(msg='请输入正确的用户名或密码'), 401

    if user_info.status != 1:
        return ops_render_err_json(msg='该用户已经被锁定，请联系管理员处理'), 401

    # 返回用户信息
    data = {
        "id": user_info.id,
        "nickname": user_info.nickname,
        "username": user_info.login_name,
        "created_time": user_info.created_time,
        "updated_time": user_info.updated_time,
    }

    # 存储登陆信息（不推荐，推荐使用插件，存储到redis等内存数据库中）
    # session['uid'] = user_info.id

    response = make_response(ops_render_json(msg='登陆成功!', data=data))
    response.set_cookie('uid', f'{UserService.get_auth_code(user_info)}#{user_info.id}', 60 * 60 * 24)

    return response


# 登出
@custom_base.route('/logout')
def logout():
    # 一个重定向的response
    response = make_response(redirect(UrlManger.build_url('/')))
    # 删除cookie
    response.delete_cookie('uid')
    # 返回response
    return response
