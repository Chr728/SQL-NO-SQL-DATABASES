import os
import json
from pathlib import Path
from pathlib import PurePath
from concurrent.futures import ProcessPoolExecutor

class JsonToQuery:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def convert_to_insert_query(self, table_name, dir_path: str, output_dir: str = '', pk=[], fn_to_add: str = None, key_name_to_add_fn: str = None):
        with open(os.path.join(dir_path, f'{table_name}.json'), encoding="utf8") as f:
            data = json.loads(f.read())

        if len(data) == 0:
            return
        
        key_list = f'({", ".join(data[0].keys())})'
        sql_statements_list = []

        for d in data:
            value = '('
            first = True
            for key in d.keys():
                if not first:
                    value += ', '
                first = False

                d[key] = str(d[key]).replace("'", "''").replace('\n', ' ').replace('\r', '')

                if fn_to_add is not None and key_name_to_add_fn is not None and key == key_name_to_add_fn:
                    value += f"{fn_to_add}({d[key]}/1000)"
                else:
                    value += f"'{d[key]}'"
                
            value += ')'
            sql_statements_list.append(f"INSERT INTO  \"{table_name}\" {key_list} VALUES {value} ON CONFLICT ({', '.join(pk)}) DO NOTHING;")

        self.save_sql_statements(table_name, output_dir if output_dir else table_name, sql_statements_list)

    def save_sql_statements(self, output_file: str, file_path: str, sql_statements_list: list) -> None:
        dir = os.path.join(self.output_dir, Path(file_path).stem)
        if not os.path.exists(dir):
            os.makedirs(dir)

        for sql_statement in sql_statements_list:
            with open(os.path.join(dir, f'insert_{output_file}.sql'), 'a+', encoding='utf-8') as f:
                f.write(sql_statement) 

    def convert_all_tables_to_insert_query(self, table_names: list, primary_keys: dict, fn_to_add: dict, key_name_to_add_fn: dict,  dir_path: str) -> None:
        last_dir = PurePath(dir_path).name
        with ProcessPoolExecutor() as executor:
            executor.map(self.convert_to_insert_query, table_names, [dir_path]*len(table_names), [last_dir]*len(table_names), [primary_keys[table_name] for table_name in table_names], [fn_to_add[table_name] for table_name in table_names], [key_name_to_add_fn[table_name] for table_name in table_names])