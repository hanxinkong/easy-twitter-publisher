# easy_twitter_publisher

推特（Twitter）发帖回帖程序，支持本地及url图文（jpg,png,gif）,视频（mp4），希望能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

----
**文档地址：
** <a href="https://easy-twitter-publisher.xink.top/" target="_blank">https://easy-twitter-publisher.xink.top/ </a>

**PyPi地址：
** <a href="https://pypi.org/project/easy-twitter-publisher" target="_blank">https://pypi.org/project/easy-twitter-publisher </a>

**GitHub地址：
** [https://github.com/hanxinkong/easy-twitter-publisher](https://github.com/hanxinkong/easy-twitter-publisher)

----

## 推特三件套（有需要可自行安装）

- `easy_twitter_publisher` 推特发帖,回帖,转载 https://pypi.org/project/easy_twitter_publisher
- `easy_twitter_crawler` 推特采集 https://pypi.org/project/easy-twitter-crawler
- `easy_twitter_interactors` 推特互动（点赞,刷阅读量等） https://pypi.org/project/easy_twitter_interactors

## 安装

<div class="termy">

```console
pip install easy-twitter-publisher
```

</div>

## 主要功能

- `media_upload` 媒体文件上传（本地图片或视频）
- `media_upload_from_url` 媒体文件上传（url链接，仅支持gif及视频）
- `post` 发帖（支持文本，图片，视频）
- `reply` 回帖（支持文本，图片，视频）

## 简单使用

设置代理及cookie (发帖和回帖均需要设置cookie)

```python
proxy = {
    'http': 'http://127.0.0.1:10808',
    'https': 'http://127.0.0.1:10808'
}
cookie = 'auth_token=686fa28f49400698820d0a3c344c51efdeeaf73a; ct0=5bed99b7faad9dcc742eda564ddbcf37888f8794abd6d4d736919234440be2172da1e9a9fc48bb068db1951d1748ba5467db2bc3e768f122794265da0a9fa6135b4ef40763e7fd91f730d0bb1298136b'
```

媒体上传使用案例（内容需要图片或视频时使用此方法）

```python
from easy_spider_tool import format_json
from easy_twitter_publisher import TwitterMedia, get_headers

twitter_media = TwitterMedia()
twitter_media.set_headers(get_headers(cookie))
twitter_media.set_proxy(proxy)
# 本地文件
media_info = twitter_media.media_upload(r'0.gif')
# 图片链接
# twitter_media.media_upload_from_url('https://th.bing.com/th/id/R.466bb61cd7cf4e8b7d9cdf645add1d6e?rik=YRZKRLNWLutoZA&riu=http%3a%2f%2f222.186.12.239%3a10010%2fwmxs_161205%2f002.jpg&ehk=WEy01YhyfNzzQNe1oIqxwgbTnzY7dMfmZZHkqpZB5WI%3d&risl=&pid=ImgRaw&r=0')
print(format_json(media_info))
```

媒体上传参数说明

| 字段名        | 类型     | 必须 | 描述     |
|------------|--------|----|--------|
| media_path | string | 是  | 媒体文件路径 |

___

发帖使用案例（指定文本，图片发帖子）

```python
from easy_spider_tool import format_json
from easy_twitter_publisher import TwitterPost, get_headers

twitter_post = TwitterPost()
twitter_post.set_headers(get_headers(cookie))
twitter_post.set_proxy(proxy)

post_info = twitter_post.post(
    text="""Hi, I'm Han Xinkong""",
    # medias=[twitter_media.media_id]
)
print(format_json(post_info))
```

发帖参数说明

| 字段名    | 类型     | 必须 | 描述                  |
|--------|--------|----|---------------------|
| text   | string | 是  | 文本（最多不超过个字符，包括空格回车） |
| medias | list   | 否  | 媒体文件上传后的媒体id（可指定多个） |              

___

回帖使用案例（指定目标帖子，对其回帖）

```python
from easy_spider_tool import format_json
from easy_twitter_publisher import TwitterPost, get_headers

twitter_post = TwitterPost()
twitter_post.set_headers(get_headers(cookie))
twitter_post.set_proxy(proxy)

reply_info = twitter_post.reply(
    to_tweet_id='1690065356495421444',
    text="""Hi, I'm Han Xinkong""",
    # medias=[twitter_media.media_id]
)
print(format_json(reply_info))
```

回帖参数说明

| 字段名         | 类型     | 必须 | 描述                                                                                     |
|-------------|--------|----|----------------------------------------------------------------------------------------|
| to_tweet_id | string | 是  | 目标帖子id（https://twitter.com/elonmusk/status/1690164670441586688 中的 1690164670441586688） |
| text        | string | 是  | 文本（最多不超过个字符，包括空格回车）                                                                    |
| medias      | list   | 否  | 媒体文件上传后的媒体id（可指定多个）                                                                    |              

___

## 依赖

内置依赖

- `typing` Type Hints for Python.
- `os` Type Hints for Python.
- `imghdr` Type Hints for Python.
- `mimetypes` Type Hints for Python.
- `pathlib` Type Hints for Python.
- `json` Type Hints for Python.

第三方依赖

- `loguru` An XPath for JSON.
- `urllib3` An XPath for JSON.
- `requests` An XPath for JSON.
- `requests_toolbelt` Python library used for parsing dates from natural language text.
- `easy_spider_tool` Python library used for parsing dates from natural language text.

_注：依赖顺序排名不分先后_

## 链接

Github：https://github.com/hanxinkong/easy-twitter-publisher

在线文档：https://easy-twitter-publisher.xink.top

## 贡献者

## 许可证

该项目根据 **MIT** 许可条款获得许可.