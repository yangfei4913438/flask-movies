import base64
import hashlib
import random
import string


class UserService():

    @staticmethod
    def get_auth_code(user_info=None):
        next_str = hashlib.md5()
        prev_str = f'{user_info.id}-{user_info.login_name}-{user_info.created_time}-{user_info.login_pwd}-{user_info.login_salt}'
        next_str.update(prev_str.encode('utf-8'))
        return next_str.hexdigest()

    @staticmethod
    def generator_salt(length=16):
        # 字符串中的asc码 + 数字，随机选择
        key_list = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        # 返回一个字符串
        return ''.join(key_list)

    @staticmethod
    def generator_pwd(pwd, salt):
        next_str = hashlib.md5()
        prev_str = f'{base64.encodebytes(pwd.encode("utf-8"))}-{salt}'
        next_str.update(prev_str.encode('utf-8'))

        return next_str.hexdigest()
