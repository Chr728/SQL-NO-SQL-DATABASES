import tweetnlp
import json

# load sentiment and emotion models
print("Opening sentiment and emotion models. Ignore the warnings that follow.")
sentimentModel = tweetnlp.load_model('sentiment')
emotionModel = tweetnlp.load_model('emotion')

# read JSON into dict
file_to_open = "reddit_posts-2023-02-03.json"
with open(file_to_open, "r") as read_file:
    print("Opening file", file_to_open)
    api_dataset = json.load(read_file)

# run sentiment and emotion analysis
for count, tweet in enumerate(api_dataset):
    print("Processing Tweet #", count + 1)
    sentimentPrediction = sentimentModel.sentiment(tweet['title'], return_probability=True)
    emotionPrediction = emotionModel.emotion(tweet['title'], return_probability=True)
    tweet['sentiment'] = sentimentPrediction
    tweet['emotion'] = emotionPrediction
    print(tweet)

# encode dict into JSON
output_filename = file_to_open[:-5] + "_analyzed" + ".json"
with open(output_filename, "w") as write_file:
    print("Writing to file", output_filename)
    json.dump(api_dataset, write_file)
