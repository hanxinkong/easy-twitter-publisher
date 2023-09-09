"""
自定义异常类
"""
from typing import Union


class ProxyException(Exception):
    """
    代理异常
    """
    pass


class CaptchaException(Exception):
    """
    验证异常
    """
    pass


class UserException(Exception):
    """
    用户异常信息
    """

    def __init__(self, user_id, msg: str = ''):
        self.user_id = user_id
        self.msg = msg

    def __str__(self):
        return f'【{self.user_id}】: {self.msg}'
