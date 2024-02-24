import tweepy

# APIキーとアクセストークンの設定
api_key='XXX'
api_key_secret='XXX'
access_token='XXX'
access_token_secret='XXX'

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# 投稿
client.create_tweet(text="テスト")

