import json
from typing import List, Dict, Optional, Union

from easy_twitter_publisher.twitter_utils.twitter_utils import request
from .constants import *


class TwitterPost(object):
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'x-twitter-auth-type': 'OAuth2Session'
    }

    def __init__(self):
        self.requests_kwargs = {}

    def set_headers(self, headers: Optional[Dict[str, str]] = None):
        if headers:
            self.default_headers.update(headers)

    def set_proxy(self, proxy: Optional[Dict[str, str]] = None):
        """
        设置代理
        :param proxy: proxy = {'http': 'http://ip:port', 'https': 'http://ip:port'}
        :return:
        """
        proxies = {
            'proxies': proxy
        }
        self.requests_kwargs.update(proxies)

    def set_timeout(self, timeout: int):
        """
        设置请求超时 单位秒
        """
        self.requests_kwargs['timeout'] = timeout

    def post(self, text: str, medias: List[Union[str, int]] = None):
        """发文"""
        api = POST_API

        medias_data = []
        if medias:
            medias_data = [{
                "media_id": f'{media_id}',
                "tagged_users": []
            } for media_id in medias]

        payload = json.dumps({
            "variables": {
                "tweet_text": f"{text}",
                "dark_request": False,
                "media": {
                    "media_entities": medias_data,
                    "possibly_sensitive": False
                },
                "semantic_annotation_ids": []
            },
            "features": {
                "tweetypie_unmention_optimization_enabled": True,
                "vibe_api_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "tweet_awards_web_tipping_enabled": False,
                "interactive_text_enabled": True,
                "responsive_web_text_conversations_enabled": False,
                "longform_notetweets_rich_text_read_enabled": True,
                "longform_notetweets_inline_media_enabled": False,
                "blue_business_profile_image_shape_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_enhance_cards_enabled": False
            },
            "queryId": "-tr9gsjcukmYZRN4dpYN8g"
        })

        response = request('POST', api, headers=self.default_headers, data=payload, **self.requests_kwargs)
        if response.status_code == 200:
            data = response.json()
            return data

    def reply(self, to_tweet_id: Union[str, int], text: str, medias: List[Union[str, int]] = None):
        """回复"""
        api = REPLY_API

        medias_data = []
        if medias:
            medias_data = [{
                "media_id": f'{media_id}',
                "tagged_users": []
            } for media_id in medias]

        payload = json.dumps({
            "variables": {
                "tweet_text": f"{text}",
                "reply": {
                    "in_reply_to_tweet_id": f"{to_tweet_id}",
                    "exclude_reply_user_ids": []
                },
                "dark_request": False,
                "media": {
                    "media_entities": medias_data,
                    "possibly_sensitive": False
                },
                "semantic_annotation_ids": []
            },
            "features": {
                "tweetypie_unmention_optimization_enabled": True,
                "vibe_api_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "tweet_awards_web_tipping_enabled": False,
                "interactive_text_enabled": True,
                "responsive_web_text_conversations_enabled": False,
                "longform_notetweets_rich_text_read_enabled": True,
                "longform_notetweets_inline_media_enabled": False,
                "blue_business_profile_image_shape_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_enhance_cards_enabled": False
            },
            "queryId": "-tr9gsjcukmYZRN4dpYN8g"
        })

        response = request('POST', api, headers=self.default_headers, data=payload, **self.requests_kwargs)
        if response.status_code == 200:
            data = response.json()
            return data