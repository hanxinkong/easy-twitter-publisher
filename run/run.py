from easy_spider_tool import format_json
from easy_twitter_publisher import TwitterMedia, TwitterPost, get_headers

proxy = {
    'http': 'http://127.0.0.1:10808',
    'https': 'http://127.0.0.1:10808'
}
cookie = 'auth_token=686fa28f49400698820d0a3c344c51e3e44af73a; ct0=5bed99b7faad9dcc742eda564ddbcf37777f8794abd6d4d736919234440be2172da1e9a9fc48bb068db1951d1748ba5467db2bc3e768f122794265da0a9fa6135b4ef40763e7fd91f730d0bb1298136b'

# 上传媒体信息（本地文件或者url）
twitter_media = TwitterMedia()
twitter_media.set_headers(get_headers(cookie))
twitter_media.set_proxy(proxy)
media_info = twitter_media.media_upload(r'0.gif')
# twitter_media.media_upload_from_url(
#     'https://th.bing.com/th/id/R.466bb61cd7cf4e8b7d9cdf645add1d6e?rik=YRZKRLNWLutoZA&riu=http%3a%2f%2f222.186.12.239%3a10010%2fwmxs_161205%2f002.jpg&ehk=WEy01YhyfNzzQNe1oIqxwgbTnzY7dMfmZZHkqpZB5WI%3d&risl=&pid=ImgRaw&r=0')
print(format_json(media_info))

# 发帖/回帖使用案例（图文发帖回帖,先上传媒体文件）
twitter_post = TwitterPost()
twitter_post.set_headers(get_headers(cookie))
twitter_post.set_proxy(proxy)

post_info = twitter_post.post(
    text="""Hi, I'm Han Xinkong""",
    medias=[twitter_media.media_id]
)
print(format_json(post_info))

reply_info = twitter_post.reply(
    to_tweet_id='1690065356495421444',
    text="""Hi, I'm Han Xinkong""",
    medias=[twitter_media.media_id]
)
print(format_json(reply_info))
