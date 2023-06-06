class User:
    def __init__(self, uid: str | int, username: str, name: str) -> None:
        self.uid = str(uid)
        self.username = username
        self.name = name

class Tweet:
    def __init__(self, tid: str | int, author_id: str | int, content: str, tweet_date: str | int, likes_number: str | int, retweets_number: str | int) -> None:
        self.tid = str(tid)
        self.author_id = str(author_id)
        self.content = content.replace("'", "''").replace(
            '\n', ' ').replace('\r', '')
        self.tweet_date = str(tweet_date)
        self.likes_number = str(likes_number)
        self.retweets_number = str(retweets_number)

class ContainsObject:
    def __init__(self, tweeter_id: str | int, hashtag_name: str) -> None:
        self.tweeter_id = str(tweeter_id)
        self.hashtag_name = hashtag_name.lower()
    
    def __str__(self) -> str:
        return f'tweeter_id: {self.tweeter_id}, hashtag_name: {self.hashtag_name}'

class Tag:
    def __init__(self, hashtag_name: str) -> None:
        self.hashtag_name = hashtag_name.lower()

class Sentiment:
    def __init__(self, sentiment_model_name: str, tweeter_id: str | int, positive_prob: str | int, negative_prob: str | int, neutral_prob: str | int) -> None:
        self.sentiment_model_name = sentiment_model_name
        self.tweeter_id =  str(tweeter_id)
        self.positive_prob =  str(positive_prob)
        self.negative_prob =  str(negative_prob)
        self.neutral_prob = str(neutral_prob)
 
class Emotion:
    def __init__(self, emotion_model_name: str, tweeter_id: str | int, anger: str | int, joy: str | int, optimism: str | int, sadness: str | int) -> None:
        self.emotion_model_name = emotion_model_name
        self.tweeter_id =  str(tweeter_id)
        self.anger_prob =  str(anger)
        self.joy_prob =  str(joy)
        self.optimism_prob = str(optimism)
        self.sadness_prob = str(sadness)

class Reddit_User:
    def __init__(self, user_name: str) -> None:
        self.user_name = str(user_name)

class Reddit_Post:
    def __init__(self, pid: str, author_name: str, title: str, url: str, subreddit: str, post_date: str | int) -> None:
        self.pid = pid
        self.author_name = author_name
        self.title = title.replace("'", "''").replace(
            '\n', ' ').replace('\r', '')
        self.url = url
        self.subreddit = subreddit
        self.post_date = str(post_date)

class Reddit_Sentiment:
    def __init__(self, sentiment_model_name: str, post_id: str, positive_prob: str | int, negative_prob: str | int, neutral_prob: str | int) -> None:
        self.sentiment_model_name = sentiment_model_name
        self.post_id =  str(post_id)
        self.positive_prob =  str(positive_prob)
        self.negative_prob =  str(negative_prob)
        self.neutral_prob = str(neutral_prob)
 
class Reddit_Emotion:
    def __init__(self, emotion_model_name: str, post_id: str | int, anger: str | int, joy: str | int, optimism: str | int, sadness: str | int) -> None:
        self.emotion_model_name = emotion_model_name
        self.post_id =  str(post_id)
        self.anger_prob =  str(anger)
        self.joy_prob =  str(joy)
        self.optimism_prob = str(optimism)
        self.sadness_prob = str(sadness)

class Data_Type:
    TWITTER_SNS_DATA = 1
    TWITTER_API_DATA = 2
    REDDIT_SNS_DATA = 3
    
def obj_dict(obj: object) -> dict:
    return obj.__dict__