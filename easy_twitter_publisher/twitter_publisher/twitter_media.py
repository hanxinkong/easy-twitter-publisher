import imghdr
import os
from typing import Any, Dict, Optional
import mimetypes
from pathlib import Path
from loguru import logger
from requests_toolbelt import MultipartEncoder
from easy_twitter_publisher.twitter_utils.twitter_utils import request
from .constants import *


class TwitterMedia(object):
    __default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-twitter-auth-type': 'OAuth2Session',
        'origin': 'https://twitter.com',
    }
    __media_type = {
        'jpeg': {
            'media_type': 'image/jpeg',
            'media_category': 'tweet_image'
        },
        'png': {
            'media_type': 'image/png',
            'media_category': 'tweet_image'
        },
        'gif': {
            'media_type': 'image/gif',
            'media_category': 'tweet_gif'
        },
    }

    def __init__(self):
        self.__total_bytes = None
        self.media_id: Optional[str, int] = None
        self.__boundary = None
        self.__info = {}
        self.__requests_kwargs = {}

    def set_headers(self, headers: Optional[Dict[str, str]] = None):
        if headers:
            self.__default_headers.update(headers)

    def set_proxy(self, proxy: Optional[Dict[str, str]] = None):
        """
        设置代理
        :param proxy: proxy = {'http': 'http://ip:port', 'https': 'http://ip:port'}
        :return:
        """
        proxies = {
            'proxies': proxy
        }
        self.__requests_kwargs.update(proxies)

    def set_timeout(self, timeout: int):
        """
        设置请求超时 单位秒
        """
        self.__requests_kwargs['timeout'] = timeout

    def __media_type_map(self, media_type: str) -> str:
        """媒体类型映射"""
        media_type = media_type.lower()
        if 'jpg' in media_type or 'jpeg' in media_type:
            return 'jpeg'
        elif 'png' in media_type:
            return 'png'
        elif 'gif' in media_type:
            return 'gif'

        return media_type

    def media_upload_from_url(self, media_url: str):
        """链接关联上传媒体,仅支持动态媒体如gif"""
        media_type = self.get_image_type_from_url(media_url)
        media_type = self.__media_type_map(media_type)
        assert media_type in 'gif', '仅支持动态媒体'

        if media_type and media_url:
            self.__init_media(media_type=media_type, source_url=media_url)

    def media_upload(self, media_path: str):
        """上传媒体文件"""
        file_path = Path(media_path)

        assert file_path.is_file(), f'【{media_path}】:请检查文件路径'

        self.get_media_bytes(media_path)
        media_type = self.get_media_type(media_path)

        if media_type and self.__total_bytes:
            self.__init_media(media_type=media_type, total_bytes=self.__total_bytes)

        if self.media_id is None: return

        self.__build_boundary(media_path)
        status_code = self.__append_media()

        if status_code != 204: return

        self.__finalize_media()
        return self.__info

    def get_media_bytes(self, media_path: str):
        """获取媒体文件大小"""
        self.__total_bytes = os.path.getsize(media_path)
        return self.__total_bytes

    def get_image_type_from_url(self, url: str) -> str:
        response = request('GET', url, stream=True, **self.__requests_kwargs)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type')
            if 'image' in content_type:
                return imghdr.what(None, h=response.content)

    @staticmethod
    def get_media_type(image_path: str):
        mime_type, _ = mimetypes.guess_type(image_path)
        return mime_type

    def __init_media(self, media_type: str, total_bytes: str = None, source_url: str = None) -> Dict[str, Any]:
        """媒体上传 初始化"""
        api = ''
        init_param = self.__media_type[self.__media_type_map(media_type)]
        if total_bytes and init_param:
            api = INIT_URL.format(total_bytes=total_bytes, **init_param)
        elif source_url and init_param:
            api = INIT_FROM_URL.format(source_url=source_url, **init_param)

        payload = {}
        response = request('POST', api, headers=self.__default_headers, data=payload, **self.__requests_kwargs)
        if response.status_code == 202:
            data = response.json()
            self.media_id = data['media_id_string']

            return data
        logger.error(f'{response.status_code}: 初始化失败')

    def __build_boundary(self, media_path: str) -> MultipartEncoder:
        """构造boundary表单数据"""
        f = open(media_path, 'rb')
        self.__boundary = MultipartEncoder(
            fields={'media': ('blob', f, 'application/octet-stream')},
            boundary='----WebKitFormBoundary7AHUvjEJioSBSVqZ'
        )
        return self.__boundary

    def __append_media(self):
        """媒体上传 追加"""
        headers = {}
        headers.update(self.__default_headers)
        headers.update({'Content-Type': self.__boundary.content_type})
        api = APPEND_URL.format(media_id=self.media_id, segment_index=0)
        payload = self.__boundary
        response = request('POST', api, headers=headers, data=payload, **self.__requests_kwargs)
        return response.status_code

    def __finalize_media(self):
        """媒体上传 完成"""
        api = FINALIZE_URL.format(media_id=self.media_id)
        payload = {}
        response = request('POST', api, headers=self.__default_headers, data=payload, **self.__requests_kwargs)
        if any([
            response.status_code == 201,
            response.status_code == 200,
        ]):
            data = response.json()
            self.__info = data
            return data
