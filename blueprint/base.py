from flask import Blueprint


# 实例化蓝图，参数：蓝图名称，导入名称
custom_base = Blueprint('custom_base', __name__)


# 基础路由
@custom_base.route('/')
def hello():
    """
    基础路由
    """
    return 'Hello World'
