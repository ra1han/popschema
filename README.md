# popschema - Synthetic Data Generator

*popschema* is a utility to generate synthetic data from a schema. No seed data is required for it.

## Getting started

- Install conda - https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
- Create conda environment using the *environment.yml* file.

## How to use

- It uses [Faker](https://faker.readthedocs.io/en/master/index.html) library to generate the synthetic data. The schema json files provide the Faker provider for each column. Example

        {
            "columns":{
                "id":{
                    "provider":"uuid"
                },
                "first_name":{
                    "provider":"first_name"
                }
            }
        }
- If a foreign key is used from another file, use fk_provider instead of provider. Example

        {
            "columns":{
                "id":{
                    "provider":"uuid"
                },
                "customer_id":{
                    "fk_provider":{
                        "fk_file": "customer.csv",
                        "fk_column": "id"
                    }
                },
                "sales":{
                    "provider":"float_100_10000"
                }
            }
        }

- If a custom provider is needed, add the custom provider class in *custom_providers.py* file and add the provider in the faker object in *main.py* file. This is how the uuid provider has been added.

*custom_providers.py*

class uuid_provider(BaseProvider):

    def uuid(self) -> str:
        return uuid.uuid4()
*main.py*

        code = f"""
    fake = Faker()
    fake.add_provider(custom_providers.float_provider)
    fake.add_provider(custom_providers.gender_provider)
    fake.add_provider(custom_providers.uuid_provider)
    val=fake.{provider}()
    """