from calculator.complex_number import ComplexNumber
from calculator.operations.operations import AdditionOperation, MultiplicationOperation, DivisionOperation
from logger.logger import log_operation

def main():
    number1 = ComplexNumber(3, 2)
    number2 = ComplexNumber(1, 4)

    addition_op = AdditionOperation()
    result_add = addition_op.calculate(number1, number2)
    log_operation("Addition", str(result_add))

    multiplication_op = MultiplicationOperation()
    result_mult = multiplication_op.calculate(number1, number2)
    log_operation("Multiplication", str(result_mult))

    division_op = DivisionOperation()
    result_div = division_op.calculate(number1, number2)
    log_operation("Division", str(result_div))

if __name__ == "__main__":
    main()
