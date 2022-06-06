from flask import Flask

# 第二个参数，指定模板的位置
app = Flask(__name__, template_folder='../templates')

# 从模块加载变量
app.config.from_object('config.base')
