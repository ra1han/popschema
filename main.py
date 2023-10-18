
import random
from faker import Faker
import json
import pandas as pd
from generator import Generator

def load_configuration(config_file):
    with open(config_file, "r") as json_file:
        return json.load(json_file)

def load_schema(schema_file):
    with open(schema_file, 'r') as file:
        return json.load(file)

def retrieve_text(df, fk_column):
    random_value = random.choice(df[fk_column])
    return random_value

def generate_fake_data(config_data, schema):
    generator = Generator(locale=config_data["locale"])

    column_names = schema["columns"].keys()
    data = pd.DataFrame(columns=column_names)

    for _ in range(config_data["count"]):
        row = {}
        for column_name in column_names:
            column_info = schema["columns"][column_name]
            if 'fk_provider' in column_info:
                fk_info = column_info['fk_provider']
                fk_file = fk_info['fk_file']
                fk_column = fk_info['fk_column']
                row[column_name] = retrieve_text(pd.read_csv(f'data/{fk_file}', delimiter='\t'), fk_column)
            else:
                provider = column_info['provider']
                row[column_name] = generator.generate_text(provider)

        data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)

    file_name = config_data["file"].replace('json', 'csv')
    data.to_csv(f'data/{file_name}', sep='\t', encoding='utf-8', index=False)

def main():
    config_data = load_configuration('config.json')
    schema = load_schema(f'schema/{config_data["file"]}')
    generate_fake_data(config_data, schema)

if __name__ == '__main__':
    main()