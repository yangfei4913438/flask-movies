from config.db import username, password, host, port, database

# 启用调试
DEBUG = True

# 连接数据库配置
SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{host}:{port}/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
