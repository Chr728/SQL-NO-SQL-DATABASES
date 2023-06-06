primary_keys = {
    "Hashtag": ["hashtag_name"],
    "Contains": ["tweeter_id", "hashtag_name"],
    "Emotion": ["tweeter_id", "emotion_model_name"],
    "Sentiment": ["tweeter_id", "sentiment_model_name"],
    "Tweet": ["tid"],
    "User": ["uid"]
}

fn_to_add = {
    "Hashtag": None,
    "Contains": None,
    "Emotion": None,
    "Sentiment": None,
    "Tweet": "to_timestamp",
    "User": None
}

key_name_to_add_fn = {
    "Hashtag": None,
    "Contains": None,
    "Emotion": None,
    "Sentiment": None,
    "Tweet": "tweet_date",
    "User": None
}

table_names = ['User', 'Tweet', 'Hashtag', 'Contains', 'Sentiment', 'Emotion']

reddit_primary_keys = {
    'RedditUser': ['user_name'],
    'RedditPost': ['pid'], 
    'RedditSentiment': ['post_id', 'sentiment_model_name'],
    'RedditEmotion': ['post_id', 'emotion_model_name']
}

reddit_fn_to_add = {
    'RedditUser': None,
    'RedditPost': 'to_timestamp', 
    'RedditSentiment': None,
    'RedditEmotion': None
}

reddit_key_name_to_add_fn = {
    'RedditUser': None,
    'RedditPost': 'post_date', 
    'RedditSentiment': None,
    'RedditEmotion': None
}

reddit_table_names = ['RedditUser', 'RedditPost', 'RedditSentiment', 'RedditEmotion']