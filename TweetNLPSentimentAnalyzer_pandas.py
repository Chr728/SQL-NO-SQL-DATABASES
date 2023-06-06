# EXTREMELY SLOW DUE TO PANDAS. DO NOT USE
import tweetnlp
import pandas

sentimentModel = tweetnlp.load_model('sentiment')
emotionModel = tweetnlp.load_model('emotion')
api_dataset = pandas.read_json('api_fetched_tweets.json', orient='id')

for count, tweet in enumerate(api_dataset):
    print("Processing Tweet #", count + 1)
    sentimentPrediction = sentimentModel.sentiment(tweet.loc[:, "text"], return_probability=True)
    emotionPrediction = emotionModel.emotion(tweet.loc[:, "text"], return_probability=True)
    tweet = tweet.append(sentimentPrediction)
    tweet = tweet.append(emotionPrediction)
    print(tweet)

api_dataset.to_json(r'tweets_with_analysis.json')
# EXTREMELY SLOW DUE TO PANDAS. DO NOT USE