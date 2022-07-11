"""
通过这个独立模块，对外提供基础变量
"""
# import subprocess
# import threading

# 获取系统的环境变量
from os import environ

from flask import Flask
from flask_assets import Bundle, Environment
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# def exec_css():
#     app.logger.info('start style monitor ...')
#     command_success = 'npm run dev'
#     subprocess.check_output([command_success], shell=True)
#
#
# thread = threading.Thread(target=exec_css)
# thread.start()

# 第二个参数，指定模板的位置(一般写相对路径)
app = Flask(__name__, template_folder='templates')
# 加载基础配置
app.config.from_object(f'config.base_setting')

# scss 文件处理
assets = Environment(app)
scss_all = Bundle('src/css/main.scss', filters='pyscss,cssmin', output='dist/css/main.css', depends='src/**/*.scss')
assets.register('scss_all', scss_all)
# 自动构建
assets.auto_build = True

# 获取环境变量
env_key = environ.get('MODE')
# 加载环境变量的配置文件
if env_key == 'dev':
    # 加载配置（必须先加载配置，否则调试工具无法启动）
    app.config.from_object('config.local_setting')
else:
    app.config.from_object('config.prod_setting')

# 只有开发环境在运行的时候，才会在环境变量中添加运行变量
if env_key == 'dev':
    # 禁止缓存
    assets.manifest = False
    assets.cache = False
    # 因 jinja 具有 cache ，所以也要設定重啟
    app.jinja_env.auto_reload = True
    # 开发环境启动调试工具
    DebugToolbarExtension(app)

# 生成数据库变量
db = SQLAlchemy(app)
