"""
接受各种参数传递的示例
"""

from flask import Blueprint, request


# 实例化蓝图，参数：蓝图名称，导入名称
custom_api = Blueprint('custom_api', __name__)


@custom_api.route('/user/<name>')
def route_param(name):
    """
    路由参数
    """
    return f'Hello {name}!'


@custom_api.route('/user')
def get_args():
    """
     url传参
    """
    name = request.args.get('name', '张三')
    return f'Hello {name}!'


@custom_api.route('/user', methods=['POST'])
def post_form_data():
    """
    POST请求，接收 form 表单数据
    Content-Type: multipart/form-data 或者 application/x-www-form-urlencoded
    """
    # post请求的处理方法中，也可以使用get方法来获取url中的参数。
    # name1 = request.args.get('name', '')
    name = request.form['name'] if 'name' in request.form else ''
    return f'Hello {name}!'


@custom_api.route('/upload', methods=['POST'])
def post_upload():
    """
    接收上传文件
    Content-Type: multipart/form-data
    """

    # 这里的file参数是前端传递过来的key
    f = request.files['file'] if "file" in request.files else ''

    # 返回数据
    return f'request:{f}'


