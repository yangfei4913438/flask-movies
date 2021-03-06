from application import app
from controller.blueprint.base import custom_base
from controller.blueprint.api import custom_api
from controller.blueprint.data import custom_data


# 注册蓝图
app.register_blueprint(custom_base, url_prefix='/')
app.register_blueprint(custom_api, url_prefix='/api')
app.register_blueprint(custom_data, url_prefix='/data')
