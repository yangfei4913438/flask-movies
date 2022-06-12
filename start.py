"""
项目入口文件
"""
# 引入控制器(控制器里面有app变量，不用单独再引入一次app)
from controller import app

if __name__ == '__main__':
    # 只有开发环境才会运行这段代码，生产不用flask自带服务器来启动项目。
    app.run('127.0.0.1', 8080)
