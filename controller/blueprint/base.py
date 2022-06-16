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


# 注册页面
@custom_base.route('/register')
def register():
    # 标题
    title = 'Home | 注册'

    return render_template('register.html', title=title)


# 登陆页面
@custom_base.route('/login')
def login():
    # 标题
    title = 'Home | 登陆'

    return render_template('login.html', title=title)
