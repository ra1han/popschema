from collections import OrderedDict
from typing import List
from faker.providers import BaseProvider
import uuid
import random

class gender_provider(BaseProvider):

    genders: OrderedDict[str, float] = OrderedDict([
        ("male", 0.4),
        ("female", 0.6)
    ])

    def gender(self) -> str:
        return self.random_elements(self.genders, length=1, use_weighting=True)[0]
    
class float_provider(BaseProvider):

    def float_100_10000(self) -> str:
        return random.uniform(100, 10000)
