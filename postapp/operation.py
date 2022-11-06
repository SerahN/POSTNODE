add_words = ['+', 'add', 'addition']
sub_words = ['-', 'subtract', 'minus', 'takeaway', 'subtraction']
div_words = ['/', 'divide', 'division']
mult_words = ['*', 'multiply', 'multiplication']

class Calculator():
    def add(x, y):
        """ add y to x """
        return x + y


    def subtract(x, y):
        """ subtract y from x"""
        return x - y


    def multiply(x, y):
        """ Multiply x and y"""
        return x * y

    def divide(x, y):
        """ Multiply x and y"""
        return x / y

class Operations():
    def operate(operator, x, y):
        operation_list = operator.split()
        for op in operation_list:
                if op in add_words:
                    op_type = "addition"
                    result = Calculator.add(x, y)
                elif op in sub_words:
                    op_type = "subtraction"
                    result = Calculator.subtract(x, y)
                elif op in div_words:
                    op_type = "division"
                    result = Calculator.divide(x, y)
                elif op in mult_words:
                    op_type = "multiplication"
                    result = Calculator.multiply(x, y)
                else:
                    return 1

                return result, op_type
