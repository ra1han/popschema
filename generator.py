from faker import Faker
import custom_providers

class Generator:
    def __init__(self, locale):
        self.fake = Faker(locale)
        self.fake.add_provider(custom_providers.gender_provider)
        self.fake.add_provider(custom_providers.float_provider)

    def generate_text(self, provider):
        if provider == 'first_name':
            return self.fake.first_name()
        if provider == 'company':
            return self.fake.company()
        if provider == 'uuid4':
            return self.fake.uuid4()
        if provider == 'last_name':
            return self.fake.last_name()
        if provider == 'gender':
            return self.fake.gender()
        if provider == 'phone_number':
            return self.fake.phone_number()
        if provider == 'job':
            return self.fake.job()
        if provider == 'address':
            return self.fake.address()
        if provider == 'float_100_10000':
            return self.fake.float_100_10000()
        if provider == 'text':
            return self.fake.text()
        
        return ''