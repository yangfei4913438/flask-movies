"""
开发环境配置
"""

# 数据库链接信息
username = 'yangfei'
password = 'Yf111111'
host = '127.0.0.1'
port = '3306'
database = 'movie'

# 开发服务器信息
DEV_HOST = '127.0.0.1'
DEV_PORT = 8080
DOMAIN = f"http://{DEV_HOST}:{DEV_PORT}"

# 當 flask 偵測到 template 有修改後，會自動去更新。
TEMPLATED_AUTO_RELOAD = True

# 运行环境
ENV = 'development'  # production

# 启用调试
DEBUG = True

# Can not compress the CSS/JS on Dev environment.
ASSETS_DEBUG = True

# flask_debugtoolbar 需要的key(随机打一串字符)
SECRET_KEY = 'dshabjdhsbahjdhwgqyw'

# 连接数据库配置
SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{host}:{port}/{database}"
# 编码格式
SQLALCHEMY_ENCODING = "utf8mb4"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = True
