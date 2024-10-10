from abc import ABC, abstractmethod
from .complex_number import ComplexNumber

class Operation(ABC):
    @abstractmethod
    def calculate(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        pass