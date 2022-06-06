from flask_sqlalchemy import SQLAlchemy
from core.application import app

# 初始化数据库
db = SQLAlchemy(app)
