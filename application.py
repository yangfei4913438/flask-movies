"""
通过这个独立模块，对外提供基础变量
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

# 第二个参数，指定模板的位置(一般写相对路径)
app = Flask(__name__, template_folder='templates')


# 加载配置（必须在生成数据库变量之前定义）
# ops_config 是环境变量值 local ｜ production
if "ops_config" in environ:
    app.config.from_object(f'config.{environ["ops_config"]}_setting')


# 生成数据库变量
db = SQLAlchemy(app)
