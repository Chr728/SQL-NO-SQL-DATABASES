import snscrape.modules.reddit as snrd
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from typing import Tuple
import pandas as pd

class RedditSearchWrapper():
    def __init__(self, key_words:str = None, date_range:Tuple = (None, None), save_json:bool = False) -> None:
        self._key_words = key_words
        self._date_range = date_range
        self._save_result_as_json = save_json
    
    def save_df_as_json(self, df:pd.DataFrame, file_name:str) -> None:
        df.to_json(file_name + '.json', orient = "records")

    def get_lower_upper_bounds(self) -> Tuple[datetime, datetime]:
        if not all(self._date_range):
            raise ValueError('Date range is not specified')
        start_date = datetime.strptime(self._date_range[0], '%Y-%m-%d')
        end_date = datetime.strptime(self._date_range[1], '%Y-%m-%d')
        return start_date, end_date      

    def break_down_date_range(self) -> list:
        date_ranges = []
        start_date, end_date = self.get_lower_upper_bounds()  
        dates = pd.date_range(start_date, end_date, freq='MS').strftime('%Y-%m-%d').tolist()
        dates.insert(0, start_date.strftime('%Y-%m-%d'))
        for i in range(len(dates) - 1):
            date_ranges.append((dates[i], dates[i+1]))
        return date_ranges
    
    def get_posts_parallel(self, limit:int = None, file_name:str = None) -> list:
        if file_name is None:
            file_name = 'default_name'
        date_ranges = self.break_down_date_range()
        with ProcessPoolExecutor() as executor:
            return list(executor.map(self.get_posts, [self._key_words] * len(date_ranges), date_ranges, [limit] * len(date_ranges), [file_name+ '-' + date_range[0] for date_range in date_ranges]))

    def get_posts(self, key_words:str = None, date_range:tuple = (None, None), limit:int = None, file_name:str = None) -> pd.DataFrame:
        if key_words is None and self._key_words is None:
            raise ValueError('Key Words not found')
        if key_words is None and self._key_words is not None:
            key_words = self._key_words
        if not all(date_range):
            date_range = self._date_range
        i = 0
        posts = []
        after_epoch = str(int(datetime.strptime(date_range[0], '%Y-%m-%d').timestamp()))
        before_epoch = str(int(datetime.strptime(date_range[1], '%Y-%m-%d').timestamp()))
        for post in snrd.RedditSearchScraper(key_words, after=after_epoch, before=before_epoch, comments=False).get_items():
            posts.append(post)
            i += 1
            if limit is not None and i == limit:
                break; 
        df = pd.DataFrame(posts)
        if self._save_result_as_json:
            self.save_df_as_json(df, file_name or 'default_name')
        return df
    
if __name__ == '__main__':
    RedditSearchWrapper(key_words='gun control', date_range=('2022-11-01', '2023-03-01'), save_json=True).get_posts_parallel(limit=5000, file_name='reddit_posts')