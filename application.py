"""
通过这个独立模块，对外提供基础变量
"""
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


# 第二个参数，指定模板的位置(一般写相对路径)
app = Flask(__name__, template_folder='templates')


# 加载配置（必须在生成数据库变量之前定义 export "ops_config"=local ）
# ops_config 是环境变量值 local ｜ prod
if "ops_config" in environ:
    # 获取环境变量
    env_key = environ.get('ops_config')

    # 加载配置（必须先加载配置，否则调试工具无法启动）
    app.config.from_object(f'config.{env_key}_setting')

    # 开发环境启动调试工具
    if env_key == 'local':
        # 调试工具
        DebugToolbarExtension(app)


# 生成数据库变量
db = SQLAlchemy(app)
