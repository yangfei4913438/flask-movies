"""
项目入口文件
"""
from application import scheduler
# 引入控制器(控制器里面有app变量，不用单独再引入一次app)
# 因为没有引入具体的变量，代码格式化会自动删除该行，而控制器是必须引入的。所以这里就这样写了。
from controller import app

from jobs.all import tasks

scheduler.add_job(func=tasks, trigger='cron', second='*/5', id='aps_test')

# 启动调度器
# 生产环境，建议是两个项目，一个纯web, 一个纯job 这样管理维护会更方便一些。（当然了，一些小的任务，也可以这样写在一起）
# 如果是超大的任务，甚至可以一个job就是一个项目。具体看任务的复杂程度。
scheduler.start()

if __name__ == '__main__':
    # 只有开发环境才会运行这段代码，生产不用flask自带服务器来启动项目。

    # 获取变量
    host = app.config.get('RUN_HOST')
    port = app.config.get('RUN_PORT')

    # 启动项目(开启调度器的时候，必须关闭DEBUG，否则任务会执行两次。。。)
    app.run(host, port, debug=False)
