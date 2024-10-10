from calculator.complex_number import ComplexNumber
class AdditionOperation:
    def calculate(self, number1: ComplexNumber, number2: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(number1.real + number2.real, number1.imaginary + number2.imaginary)

class MultiplicationOperation:
    def calculate(self, number1: ComplexNumber, number2: ComplexNumber) -> ComplexNumber:
        real = number1.real * number2.real - number1.imaginary * number2.imaginary
        imaginary = number1.real * number2.imaginary + number1.imaginary * number2.real
        return ComplexNumber(real, imaginary)

class DivisionOperation:
    def calculate(self, number1: ComplexNumber, number2: ComplexNumber) -> ComplexNumber:
        denominator = number2.real**2 + number2.imaginary**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        real = (number1.real * number2.real + number1.imaginary * number2.imaginary) / denominator
        imaginary = (number1.imaginary * number2.real - number1.real * number2.imaginary) / denominator
        return ComplexNumber(real, imaginary)
