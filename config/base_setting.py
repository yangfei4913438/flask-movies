"""
基础配置
"""
from os import path

# 版本文件的路径(这里只是演示文件的获取，正常情况下，直接写版本号作为变量就行了)
RELEASE_PATH = path.join(path.dirname(path.dirname(__file__)), 'release_version')
