from abc import ABC, abstractmethod
from .complex_number import ComplexNumber

class Operation(ABC):
    @abstractmethod
    def calculate(self, number1: ComplexNumber, number2: ComplexNumber) -> ComplexNumber:
        pass
