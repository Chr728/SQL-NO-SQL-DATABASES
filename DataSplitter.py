import os
import json
from pathlib import Path
from utils.dataclasses  import Data_Type
from utils.dataclasses  import User
from utils.dataclasses  import Tweet
from utils.dataclasses  import Sentiment
from utils.dataclasses  import Emotion
from utils.dataclasses  import ContainsObject
from utils.dataclasses  import Tag
from utils.dataclasses  import Reddit_User
from utils.dataclasses  import Reddit_Post
from utils.dataclasses  import Reddit_Sentiment
from utils.dataclasses  import Reddit_Emotion
from utils.dataclasses  import obj_dict
from concurrent.futures import ProcessPoolExecutor

class DataSplitter:

    def __init__(self, output_dir: str, data_type: int = Data_Type.TWITTER_SNS_DATA) -> None:
        self.output_dir = output_dir
        self.data_type = data_type
    
    def split_data_parallel(self, file_paths: list) -> None:
        with ProcessPoolExecutor() as executor:
            executor.map(self.split_data, file_paths)

    def split_data(self, file_path: str, table_names: list = []) -> None:
        user_list = list()
        post_list = list()
        hashtag_set = set()
        contains_list = list()
        sentiment_list = list()
        emotion_list = list()
        
        with open(file_path, encoding="utf8") as data_file:
            data = json.load(data_file)
            for entry in data:
                if self.data_type == Data_Type.TWITTER_SNS_DATA:
                    user_list.append(User(entry['user']['id'], entry['user']['username'], entry['user']['displayname']))
                    post_list.append(Tweet(entry['id'], entry['user']['id'], entry['renderedContent'], entry['date'], entry['likeCount'], entry['retweetCount']))
                    hashtag_set.update(entry['hashtags'] if entry['hashtags'] else [])
                    contains_list.extend([ContainsObject(entry['id'], hashtag_name) for hashtag_name in (entry['hashtags'] if entry['hashtags'] else [])])
                    sentiment_list.append(Sentiment('tweetnlp',entry['id'], entry['sentiment']['probability']['positive'], entry['sentiment']['probability']['negative'], entry['sentiment']['probability']['neutral']))                
                    emotion_list.append(Emotion('tweetnlp',entry['id'], entry['emotion']['probability']['anger'], entry['emotion']['probability']['joy'], entry['emotion']['probability']['optimism'], entry['emotion']['probability']['sadness']))                
                elif self.data_type == Data_Type.TWITTER_API_DATA:
                    user_list.append(User(entry['author_id']['id'], entry['author_id']['username'], entry['author_id']['username']))
                    post_list.append(Tweet(entry['id'], entry['author_id']['id'], entry['text'], entry['created_at'], entry['public_metrics']['like_count'], entry['public_metrics']['retweet_count']))
                    if entry['entities'] is not None and entry['entities'].get('hashtags', None) is not None:
                        hashtag_set.update([hashtag['tag'] for hashtag in entry['entities']['hashtags']])
                        contains_list.extend([ContainsObject(entry['id'], hashtag['tag']) for hashtag in entry['entities']['hashtags']])
                    sentiment_list.append(Sentiment('tweetnlp',entry['id'], entry['sentiment']['probability']['positive'], entry['sentiment']['probability']['negative'], entry['sentiment']['probability']['neutral']))                
                    emotion_list.append(Emotion('tweetnlp',entry['id'], entry['emotion']['probability']['anger'], entry['emotion']['probability']['joy'], entry['emotion']['probability']['optimism'], entry['emotion']['probability']['sadness']))                
                elif self.data_type == Data_Type.REDDIT_SNS_DATA:
                    user_list.append(Reddit_User(entry['author']))
                    post_list.append(Reddit_Post(entry['id'], entry['author'], entry['title'], entry['url'], entry['subreddit'], entry['date']))
                    sentiment_list.append(Reddit_Sentiment('tweetnlp',entry['id'], entry['sentiment']['probability']['positive'], entry['sentiment']['probability']['negative'], entry['sentiment']['probability']['neutral']))                
                    emotion_list.append(Reddit_Emotion('tweetnlp',entry['id'], entry['emotion']['probability']['anger'], entry['emotion']['probability']['joy'], entry['emotion']['probability']['optimism'], entry['emotion']['probability']['sadness']))                
                else:
                    raise ValueError('Unknown Data Type')
                
        self.save_data(file_path, table_names=table_names, user_list=user_list, post_list=post_list, hashtag_set=hashtag_set, contains_list=contains_list, sentiment_list=sentiment_list, emotion_list=emotion_list)

    def save_data(self, file_path: str, table_names: list = [], **kwargs) -> None:
        dir = os.path.join(self.output_dir, Path(file_path).stem)
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        user_list = kwargs.get('user_list', list())
        post_list = kwargs.get('post_list', list())
        hashtag_set = kwargs.get('hashtag_set', set())
        contains_list = kwargs.get('contains_list', list())
        sentiment_list = kwargs.get('sentiment_list', list())
        emotion_list = kwargs.get('emotion_list', list())

        for output_file in table_names:
            with open(os.path.join(dir, f'{output_file}.json'), 'w+', encoding='utf-8') as f:
                if (output_file == 'User' or output_file == 'RedditUser') and len(user_list) > 0:
                    json.dump(user_list,f, default=obj_dict, ensure_ascii=False)
                elif (output_file == 'Tweet' or output_file == 'RedditPost') and len(post_list) > 0:
                    json.dump(post_list,f, default=obj_dict, ensure_ascii=False)                
                elif output_file == 'Hashtag' and len(hashtag_set) > 0:
                    json.dump([Tag(hashtag) for hashtag in hashtag_set], f, default=obj_dict, ensure_ascii=False)
                elif output_file == 'Contains' and len(contains_list) > 0:
                    json.dump(contains_list,f, default=obj_dict, ensure_ascii=False)
                elif (output_file == 'Sentiment' or output_file == 'RedditSentiment') and len(sentiment_list) > 0:
                    json.dump(sentiment_list,f, default=obj_dict, ensure_ascii=False)
                elif (output_file == 'Emotion' or output_file == 'RedditEmotion') and len(emotion_list) > 0:
                    json.dump(emotion_list,f, default=obj_dict, ensure_ascii=False)          