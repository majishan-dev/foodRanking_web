import tweepy

# APIキーとアクセストークンの設定
api_key = "dacvLO8mPZm5GkKAhwmg4fk2M"
api_key_secret = "rmkOggB1CNFeJOllkweVQx11mgPgneMuiQh8uSEhLEdUIf4xpM"
access_token = "849501462011023360-2sVFHcjhSPQdICYOqJtrMhrm5k2YnW9"
access_token_secret = "jMA1Lp9ZOws4bbbGXzqkEdQnBxAOkBPaI72hwK5SPrHa0"

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# 投稿
client.create_tweet(text="テスト")
