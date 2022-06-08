from flask import render_template
from application import app


@app.errorhandler(404)
def err_404(e):
    """
    拦截404页面
    参数e, 是必填的形参，否则会报错。
    """
    return render_template('404.html')
