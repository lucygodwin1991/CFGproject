import tweepy

auth = tweepy.OAuthHandler('gdT9Z3Pt22LAaM6EBJ6ZsPmXw','aSlc67r2NCSG4gjhTa8IbY4O4fQ5XXCfTZsFaCJubfqLkdPS07')
auth.set_access_token('24850991-qmvMhxBqSGMGGqvAlzIV4osP85rfO22l949b2NbtZ','f4JHDn2GjB7Ez5QMOyDAmTjMPoV2h7IOsQeTJpIQnzP52')

twitter_api = tweepy.API('auth')

cfg_tweets = twitter_api.search(
    q="CodeFirstGirls"
)

for tweet in cfg_tweets:
    print tweet.user.name + ": " + tweet.text
