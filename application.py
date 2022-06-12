"""
通过这个独立模块，对外提供基础变量
"""
import subprocess
import threading
from os import environ

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# 第二个参数，指定模板的位置(一般写相对路径)
app = Flask(__name__, template_folder='templates')

# 加载配置（必须在生成数据库变量之前定义 export "ops_config"=local , 检查 echo $ops_config）
# ops_config 是环境变量值 local ｜ prod
if "ops_config" in environ:
    # 获取环境变量
    env_key = environ.get('ops_config')

    # 加载配置（必须先加载配置，否则调试工具无法启动）
    app.config.from_object(f'config.{env_key}_setting')

    # 开发环境启动调试工具
    if env_key == 'local':
        # 因 jinja 具有 cache ，所以也要設定重啟
        app.jinja_env.auto_reload = True
        # 调试工具
        DebugToolbarExtension(app)


        def exec_css():
            app.logger.info('start style monitor ...')
            command_success = 'npm run dev'
            subprocess.check_output([command_success], shell=True)
 

        thread = threading.Thread(target=exec_css)
        thread.start()

    else:
        def exec_css():
            app.logger.info('build css ....')
            command_success = 'npm run build'
            subprocess.check_output([command_success], shell=True)


        thread = threading.Thread(target=exec_css)
        thread.start()

# 生成数据库变量
db = SQLAlchemy(app)
