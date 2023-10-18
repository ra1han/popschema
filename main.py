
import datetime
from faker import Faker
import uuid
import custom_providers
import json
import pandas as pd
from generator import Generator

def retrieve_text(fk_file, fk_column):
    df = pd.read_csv(f'data/{fk_file}', delimiter='\t')
    random_value = df[fk_column].sample().values[0]

    return random_value

def main():

    with open('config.json', "r") as json_file:
        config_data = json.load(json_file)

    schema_file = config_data["file"]
    record_count = config_data["count"]

    with open(f'schema/{schema_file}', 'r') as file:
        schema = json.load(file)

    locale_list = ['en-US']
    generator = Generator(locale=locale_list)

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
                row[column_name] = generator.generate_text(provider)

        data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)

    file_name = schema_file.replace('json','csv')
    data.to_csv(f'data/{file_name}', sep='\t', encoding='utf-8', index=False)

if __name__ == '__main__':
    main()