"""
项目入口文件
"""

# 引入蓝图(蓝图里面有app变量，不用单独再引入一次app)
from blueprint import app


def main():
    # 启动 DEBUG 才会打印日志
    app.logger.info('================= 项目开始运行 =================')
    app.run('0.0.0.0', 8080)
    app.logger.warning('================= 项目停止运行 =================')


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
