# 蓝图
from controller.blueprint import *
# 拦截器
from controller.interceptor import *

# 加载模板函数
from lib.urlManager import UrlManger

# 注册函数到模板
app.add_template_global(UrlManger.build_static_url, 'buildStaticUrl')
app.add_template_global(UrlManger.build_url, 'buildUrl')
