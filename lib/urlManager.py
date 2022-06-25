import os.path

from application import app, env_key
from utils.dateHelper import get_current_time


class UrlManger(object):

    @staticmethod
    def build_url(path):
        """
        获取基于完整URL的绝对路径
        """
        domain = app.config['DOMAIN']
        return f"{domain}{path}"

    @staticmethod
    def build_static_url(path):
        """
        完整路径的静态资源
        """
        full_path = f"/static{path}?ver={UrlManger.get_release_version()}"
        return UrlManger.build_url(full_path)

    @staticmethod
    def get_release_version():
        # 判断当前的环境变量
        if env_key == 'dev':
            # 开发环境，版本号使用变量，确保文件可以一直变化
            return get_current_time('%Y%m%d%H%M%S%f')
        else:
            # 生产环境，版本号从文件中获取
            release_path = app.config.get('RELEASE_PATH')
            if release_path and os.path.exists(release_path):
                # 打开文件
                with open(release_path, 'r') as f:
                    # 读取一行
                    return f.readline()
