import os
from DataSplitter import DataSplitter
from RemoveDuplicate import RemoveDuplicate
from JSONToQuery import JsonToQuery
from concurrent.futures import ProcessPoolExecutor
from utils.dataclasses import Data_Type
from utils.schemadescription import reddit_primary_keys
from utils.schemadescription import reddit_table_names
from utils.schemadescription import reddit_fn_to_add
from utils.schemadescription import reddit_key_name_to_add_fn

DATA_TYPE = Data_Type.REDDIT_SNS_DATA
DATA_DIR = 'raw_data/reddit_data/'
DATA_FILE_NAME = ['reddit_posts-2022-11-03_analyzed', 'reddit_posts-2022-12-03_analyzed', 
                  'reddit_posts-2023-01-03_analyzed','reddit_posts-2023-02-03_analyzed']
DATA_FILE_TYPE = 'json'

PRIMARY_KEYS = reddit_primary_keys
TABLE_NAMES = reddit_table_names
FN_TO_ADD = reddit_fn_to_add
KEY_NAME_TO_ADD_FN = reddit_key_name_to_add_fn

DATA_SPLITTER_OUTPUT_DIR = 'output-broken-data'
REMOVE_DUPLICATE_OUTPUT_DIR = 'unique_data'
JSON_TO_QUERY_OUTPUT_DIR = 'insert_queries'

TRACE = True

def log(info: str = None):
    if (TRACE):
        print(info)

def process_file(data_file_name):
    if DATA_FILE_TYPE != 'json':
        raise ValueError(f'{data_file_name}) DATA FILE TYPE must be JSON')

    log(f'{data_file_name}) STEP 1 of 3: Splitting the data: Starting')
    if type(data_file_name) is str:
        DataSplitter(DATA_SPLITTER_OUTPUT_DIR, DATA_TYPE).split_data(os.path.join(DATA_DIR, f'{data_file_name}.{DATA_FILE_TYPE}'), TABLE_NAMES)
    else:
        raise ValueError(f'{data_file_name}) DATA FILE NAME must be a string')
    log(f'{data_file_name}) STEP 1 of 3: Splitting the data: Completed')

    log(f'{data_file_name}) STEP 2 of 3: Removing duplicate data: Starting')
    if type(PRIMARY_KEYS) is dict and type(TABLE_NAMES) is list:
        RemoveDuplicate(REMOVE_DUPLICATE_OUTPUT_DIR).remove_duplicates_all_tables(TABLE_NAMES, PRIMARY_KEYS, os.path.join(DATA_SPLITTER_OUTPUT_DIR, data_file_name))
    elif (type(PRIMARY_KEYS) is list or type(PRIMARY_KEYS is str)) and type(TABLE_NAMES) is str:
        RemoveDuplicate(REMOVE_DUPLICATE_OUTPUT_DIR).remove_duplicate(TABLE_NAMES, PRIMARY_KEYS, os.path.join(DATA_SPLITTER_OUTPUT_DIR, data_file_name, f'{TABLE_NAMES}')) 
    else:
        raise ValueError(f'{data_file_name}) PRIMARY KEYS must be a dictionary or a list of string or a string\nTABLE NAMES must be a list of strings or a string')
    log(f'{data_file_name}) STEP 2 of 3: Removing duplicate data: Starting:  Completed')

    log(f'{data_file_name}) STEP 3 of 3: Converting the JSON into INSERT queries: Starting')
    if type(PRIMARY_KEYS) is dict and type(TABLE_NAMES) is list and type(FN_TO_ADD) is dict and type(KEY_NAME_TO_ADD_FN) is dict:
        JsonToQuery(JSON_TO_QUERY_OUTPUT_DIR).convert_all_tables_to_insert_query(TABLE_NAMES, PRIMARY_KEYS, FN_TO_ADD, KEY_NAME_TO_ADD_FN, os.path.join(REMOVE_DUPLICATE_OUTPUT_DIR, data_file_name))
    elif (type(PRIMARY_KEYS) is list or type(PRIMARY_KEYS is str)) and type(TABLE_NAMES) is str and (FN_TO_ADD is None or type(FN_TO_ADD) is str) and (KEY_NAME_TO_ADD_FN is None or type(KEY_NAME_TO_ADD_FN) is str):
        JsonToQuery(JSON_TO_QUERY_OUTPUT_DIR).convert_to_insert_query(TABLE_NAMES, os.path.join(REMOVE_DUPLICATE_OUTPUT_DIR, data_file_name), TABLE_NAMES, PRIMARY_KEYS, FN_TO_ADD, KEY_NAME_TO_ADD_FN)
    else:
        raise ValueError(f'{data_file_name}) PRIMARY KEYS must be a dictionary or a list of string or a string\nTABLE NAMES must be a list of strings or a string\nFN TO ADD must a dict or a string or none\KEY NAME TO ADD FN must a dict or a string or none')
    log(f'{data_file_name}) STEP 3 of 3: Converting the JSON into INSERT queries: DONE')

    print(f'{data_file_name}) Data can now be inserted into the database by copying the INSERT qsueries')

def process_files_parallel(data_files: list = []):
    if type(data_files) is not list:
        raise ValueError('DATA FILES must be a list of strings')
    with ProcessPoolExecutor() as executor:
        executor.map(process_file, data_files)

if __name__ == '__main__':
    if type(DATA_FILE_NAME) is str:
        process_file(DATA_FILE_NAME)
    else:
        process_files_parallel(DATA_FILE_NAME)