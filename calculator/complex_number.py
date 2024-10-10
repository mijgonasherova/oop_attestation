class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"