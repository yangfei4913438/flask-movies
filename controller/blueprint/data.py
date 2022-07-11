"""
返回各种数据的示例
"""

from flask import Blueprint, jsonify, make_response

from model.user import User
from utils.helper import auth_render

# 实例化蓝图，参数：蓝图名称，导入名称
custom_data = Blueprint('custom_data', __name__)


@custom_data.route('/')
def json_data():
    """
    返回JSON格式的数据
    """
    data = {"name": "张三", "age": 18}
    response = make_response(jsonify(data))
    return response


@custom_data.route('/users')
def user_info():
    """
    数据库原生查询
    """

    # 查询的结果，每行一个元组返回一个列表
    users = User.query.all()

    # 渲染模板
    return auth_render('users.html', users=users)
