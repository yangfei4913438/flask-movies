from flask import g, request

from application import app
from lib.UserService import UserService
from model.user import User


@app.before_request
def before():
    """
    请求之前执行
    """
    app.logger.info('------before_request------')
    user_info = check_login()
    app.logger.info(user_info)

    # 全局变量，放到模板中去
    g.current_user = None
    if user_info:
        g.current_user = user_info


@app.after_request
def after(response):
    """
    请求之后执行
    """
    app.logger.info('------after_request------')
    return response


# 判断用户是否登陆
def check_login():
    cookies = request.cookies
    uid = cookies['uid'] if 'uid' in cookies else None

    if uid is None:
        return False

    auth_info = uid.split('#')
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if auth_info[0] != UserService.get_auth_code(user_info):
        return False

    return user_info
