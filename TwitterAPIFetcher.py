import sys
import tweepy
import pandas as pd
from os import environ, path
from datetime import datetime
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

bearer_token = environ.get('BEARER_TOKEN')

limit = 10
query = '"gun control" lang:en -is:retweet -is:reply -is:quote'
tweet_fields = ['created_at', 'public_metrics', 'author_id', 'entities']
user_fields = ['name', 'username']
expansions = 'author_id'
tweets = []
next_token = ''

if (len(sys.argv) >= 2):
    next_token = sys.argv[1]
    print(f'starting at {next_token}')

client = tweepy.Client(bearer_token)

for response in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100, tweet_fields=tweet_fields, user_fields=user_fields, expansions=expansions, next_token=next_token, limit=limit):
    data_tweets = response.data
    data_users = {user["id"]: user for user in response.includes.get('users')}
    next_token = response[3].get('next_token')
    
    for tweet in data_tweets:
        author = data_users[tweet.author_id]
        tweet.author_id = author.data
        tweets.append(tweet)

df = pd.DataFrame(tweets)
df.to_json(f'api_fetched_tweets_{datetime.now().strftime("%Y%m%d%H%M%S")}.json', orient="records")
print('finished')
print(f'next-token is {next_token}')
