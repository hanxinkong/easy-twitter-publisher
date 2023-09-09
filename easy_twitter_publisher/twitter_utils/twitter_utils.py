""""
推特工具类
"""
from typing import Dict

import requests
import urllib3
from easy_spider_tool import cookie_to_dic
from loguru import logger
from requests import Response, RequestException

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bearer = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'


def get_proxy():
    """
    获取代理
    """
    proxy_meta = {
        'http': 'http://127.0.0.1:10808',
        'https': 'http://127.0.0.1:10808'
    }
    return proxy_meta


def get_headers(cookie: str):
    assert cookie, '必须设置正确的cookie'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
        'content-type': 'application/json',
        'x-twitter-active-user': 'yes',
        # 'x-twitter-auth-type': 'OAuth2Session',
        'authorization': bearer,
        'x-csrf-token': cookie_to_dic(cookie)['ct0'],
        'cookie': cookie,
    }

    return headers


class MaxRequestRetryCount(Exception):
    pass


def request(method: str, url: str, headers: Dict[str, str] = None, retry_num: int = 3, **kwargs) -> Response:
    retry_count = 0
    while retry_num >= retry_count:
        try:
            return requests.request(method.lower(), url, headers=headers, verify=False, **kwargs)

        except RequestException as rex:
            logger.error(
                f'request exception: {rex}' + f', kwargs: {kwargs}, next retry ...' if retry_count < retry_num else 'exit retry')
            retry_count += 1

    raise MaxRequestRetryCount(f'retry count: {retry_count}')
