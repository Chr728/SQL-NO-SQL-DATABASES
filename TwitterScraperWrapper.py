import snscrape.modules.twitter as sntwt
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from typing import Tuple
import pandas as pd
import re

class TweetSearchWrapper():
    def __init__(self, query:str = None, save_json:bool = False) -> None:
        self._query = query
        self._save_result_as_json = save_json
    
    def save_df_as_json(self, df:pd.DataFrame, file_name:str) -> None:
        df.to_json(file_name + '.json', orient = "records")

    def get_lower_upper_bounds(self) -> Tuple[datetime, datetime]:
        if self._query is None:
            raise ValueError('Query not found')
        if re.search('^(?=.*until)(?=.*since).*$', self._query) is None:
            raise ValueError('Query does not contain date boundaries')
        lower_bound_str = re.search('since:\d{4}-\d{2}-\d{2}', self._query).group(0)[6:]
        upper_bound_str = re.search('until:\d{4}-\d{2}-\d{2}', self._query).group(0)[6:]
        start_date = datetime.strptime(lower_bound_str, '%Y-%m-%d')
        end_date = datetime.strptime(upper_bound_str, '%Y-%m-%d')
        return start_date, end_date      

    def break_down_query(self) -> list:
        queries = []
        start_date, end_date = self.get_lower_upper_bounds()  
        dates = pd.date_range(start_date, end_date, freq='MS').strftime('%Y-%m-%d').tolist()
        for i in range(len(dates) - 1):
            temp_query = re.sub('since:\d{4}-\d{2}-\d{2}', 'since:' + dates[i], self._query)
            temp_query = re.sub('until:\d{4}-\d{2}-\d{2}', 'until:' + dates[i + 1], temp_query)
            queries.append(temp_query)
        return queries

    def preprocess_tweet(self, tweet:object) -> object:
        '''
            Not done: depends on what type of analysis will be done
        '''
        tweet.renderedContent = tweet.renderedContent.replace('\n', ' ')
        return tweet

    def get_tweets_parallel(self, limit:int = None, file_name:str = None) -> list:
        if file_name is None:
            file_name = 'default_name'
        queries = self.break_down_query()
        with ProcessPoolExecutor() as executor:
            return list(executor.map(self.get_tweets, queries, [limit] * len(queries), [file_name+ '-' + re.search('since:\d{4}-\d{2}-\d{2}', query).group(0)[6:] for query in queries]))

    def get_tweets(self, query:str = None, limit:int = None, file_name:str = None) -> pd.DataFrame:
        if query is None and self._query is None:
            raise ValueError('Query not found')
        if query is None and self._query is not None:
            query = self._query
        i = 0
        tweets = []
        for tweet in sntwt.TwitterSearchScraper(query).get_items():
            tweets.append(self.preprocess_tweet(tweet))
            i += 1
            if limit is not None and i == limit:
                break; 
        df = pd.DataFrame(tweets)
        if self._save_result_as_json:
            self.save_df_as_json(df, file_name or 'default_name')
        return df
    
if __name__ == '__main__':
    query = '"gun control" lang:en since:2020-02-01 until:2021-12-01 -filter:replies -filter:nativeretweets'
    TweetSearchWrapper(query, save_json=True).get_tweets_parallel(limit=5000, file_name='tweets')