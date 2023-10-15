
import datetime
from faker import Faker
import uuid
import custom_providers
import json
import pandas as pd

def gen_text(provider):
    code = f"""
fake = Faker()
fake.add_provider(custom_providers.float_provider)
fake.add_provider(custom_providers.gender_provider)
fake.add_provider(custom_providers.uuid_provider)
val=fake.{provider}()
"""
    loc = {}
    exec(code, globals(), loc)
    val = loc['val']

    return val

def retrieve_text(fk_file, fk_column):
    df = pd.read_csv(f'data/{fk_file}', delimiter='\t')
    random_value = df[fk_column].sample().values[0]

    return random_value

def main():
    schema_file = 'sales.json'
    record_count = 10
    with open('schema/sales.json', 'r') as file:
        schema = json.load(file)

    locale_list = ['en-US']
    fake = Faker(locale_list)
    fake.add_provider(custom_providers.gender_provider)

    column_names = schema["columns"].keys()
    data = pd.DataFrame(columns=column_names)

    for i in range(record_count):
        row = {}
        for column_name in column_names:
            if 'fk_provider' in schema["columns"][column_name]:
                fk_file = schema["columns"][column_name]['fk_provider']['fk_file']
                fk_column = schema["columns"][column_name]['fk_provider']['fk_column']

                row[column_name] = retrieve_text(fk_file, fk_column)
            else:
                provider = schema["columns"][column_name]['provider']
                row[column_name] = gen_text(provider)

        data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)

    file_name = schema_file.replace('json','csv')
    data.to_csv(f'data/{file_name}', sep='\t', encoding='utf-8', index=False)

if __name__ == '__main__':
    main()