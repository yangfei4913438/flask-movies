from flask import make_response, render_template, jsonify
from sqlalchemy import text
from core.database import db
from core.application import app
from router.api_blueprint import api


# 注册蓝图，使用url前缀（不影响正常的路由）
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def hello():
    """
    基础路由
    """
    return 'Hello World'


@app.route('/data')
def json_data():
    """
    返回JSON格式的数据
    """
    data = {"name": "张三", "age": 18}
    response = make_response(jsonify(data))
    return response


@app.route('/users')
def user_info():
    """
    数据库原生查询
    """
    # 构建查询语句
    sql = text(f'select Host, User from user')

    # 查询的结果，每行一个元组返回一个列表
    users = db.engine.execute(sql)

    # 渲染模板
    return render_template('users.html', users=users)
