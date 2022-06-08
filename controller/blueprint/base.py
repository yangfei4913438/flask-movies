from flask import Blueprint, render_template


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
