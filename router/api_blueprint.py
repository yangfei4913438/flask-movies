from flask import Blueprint, request


# 实例化蓝图，参数：蓝图名称，导入名称
api = Blueprint('custom_api', __name__)


# 这里的用法和普通的路由装饰器一致。
@api.route('/')
def home():
    """
    蓝图 api 首页
    """
    return 'home page'


@api.route('/say/<name>')
def say(name):
    """
    路由参数
    """
    return f'Hello {name}!'


@api.route('/student')
def info():
    """
     url传参
    """
    name = request.args.get('name', '张三')
    return f'这位同学的名字: {name}'


@api.route('/student', methods=['POST'])
def update_info():
    """
    POST请求，接收 form 表单数据
    Content-Type: multipart/form-data 或者 application/x-www-form-urlencoded
    """
    # post请求的处理方法中，也可以使用get方法来获取url中的参数。
    # name1 = request.args.get('name', '')
    name = request.form['name'] if 'name' in request.form else ''
    return f'接收到的名称: {name}'


@api.route('/upload', methods=['POST'])
def upload():
    """
    接收上传文件
    Content-Type: multipart/form-data
    """

    # 这里的file参数是前端传递过来的key
    f = request.files['file'] if "file" in request.files else ''

    # 返回数据
    return f'request:{f}'


