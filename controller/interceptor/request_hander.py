from application import app


@app.before_request
def before():
    """
    请求之前执行
    """
    app.logger.info('------before_request------')


@app.after_request
def after(response):
    """
    请求之后执行
    """
    app.logger.info('------after_request------')
    return response
