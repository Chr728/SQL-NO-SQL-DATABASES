import os
import json
from pathlib import Path
from pathlib import PurePath
from concurrent.futures import ProcessPoolExecutor

class RemoveDuplicate:

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def remove_duplicate(self, table_name: str, primary_keys: list, file_path: str, output_dir: str = None) -> None:
        unique_data = set()
        with open(file_path, encoding="utf8") as data_file:
            data = json.load(data_file)
            unique_data = {'-'.join([str(x[key]) for key in primary_keys]): x for x in data}
        
        self.save_data(table_name, output_dir if output_dir else file_path, unique_data)

    def save_data(self, output_file: str, file_path: str, data: set) -> None:
        dir = os.path.join(self.output_dir, Path(file_path).stem)
        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(os.path.join(dir, f'{output_file}.json'), 'w+', encoding='utf-8') as f:
            json.dump(list(data.values()), f, ensure_ascii=False)

    def remove_duplicates_all_tables(self, table_names: list, primary_keys: dict, dir_path: str = '') -> None:
        last_dir = PurePath(dir_path).name
        with ProcessPoolExecutor() as executor:
            executor.map(self.remove_duplicate, table_names, [primary_keys[table_name] for table_name in table_names], [os.path.join(dir_path, f'{table_name}.json') for table_name in table_names], [last_dir]*len(table_names))