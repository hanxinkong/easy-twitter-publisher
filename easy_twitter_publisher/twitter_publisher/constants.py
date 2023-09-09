# 媒体上传 初始化
INIT_URL = "https://upload.twitter.com/i/media/upload.json?command=INIT&total_bytes={total_bytes}&media_type={media_type}&media_category={media_category}"
INIT_FROM_URL = "https://upload.twitter.com/i/media/upload.json?command=INIT&source_url={source_url}&media_type={media_type}&media_category={media_category}"
# 媒体上传 追加
APPEND_URL = 'https://upload.twitter.com/i/media/upload.json?command=APPEND&media_id={media_id}&segment_index={segment_index}'
# 媒体上传 完成
FINALIZE_URL = "https://upload.twitter.com/i/media/upload.json?command=FINALIZE&media_id={media_id}"
# 媒体上传 状态/进度
STATUS_URL = 'https://upload.twitter.com/i/media/upload.json?command=STATUS&media_id={media_id}'
# 发帖
POST_API = "https://twitter.com/i/api/graphql/-tr9gsjcukmYZRN4dpYN8g/CreateTweet"
# 回帖
REPLY_API = 'https://twitter.com/i/api/graphql/-tr9gsjcukmYZRN4dpYN8g/CreateTweet'
