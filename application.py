"""
通过这个独立模块，对外提供基础变量
"""
# import subprocess
# import threading
from os import environ

from flask import Flask
from flask_assets import Bundle, Environment
# from flask_debugtoolbar import DebugToolbarExtension
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

# scss 文件处理
assets = Environment(app)
scss_all = Bundle('src/css/main.scss', filters='pyscss,cssmin', output='dist/css/main.css',
                  depends='src/**/*.scss')
assets.register('scss_all', scss_all)
js_all = Bundle('src/js/jquery-3.6.0.min.js', 'src/js/bootstrap.min.js', filters='jsmin',
                output='dist/js/main.js')
assets.register('js_all', js_all)
# 禁止缓存
assets.manifest = False
assets.cache = False
assets.auto_build = True

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
        # DebugToolbarExtension(app)

# 生成数据库变量
db = SQLAlchemy(app)
