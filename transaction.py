# Base Transaction class (Inheritance)
from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

        @abstractmethod
        def process(self):
            pass