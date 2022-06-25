from datetime import datetime


def get_current_time(fmt="%Y-%m-%d %H:%M:%S"):
    """
    获取当前时间字符串(1970-01-01 00:00:00)
    """

    dt = datetime.now()

    return dt.strftime(fmt)
