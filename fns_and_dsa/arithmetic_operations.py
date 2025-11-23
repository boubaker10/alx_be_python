# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or an error message string
        if division by zero occurs or the operation is invalid.
    """

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            # Division by zero handling
            return "Error: Division by zero is not allowed."
        return num1 / num2

    # Invalid operation handling
    return "Error: Invalid operation. Choose add, subtract, multiply, or divide."
