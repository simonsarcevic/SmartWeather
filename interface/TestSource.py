import random
from abc import ABC

from interface.Source import Source

class TestSource(Source, ABC):
    def __init__(self):
        self.value = random.randint(0, 100)

    def show(self):
        print(f"Test Value: {self.value}")

    def refresh(self):
        self.value = random.randint(0, 100)