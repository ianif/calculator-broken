def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If the divisor (b) is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

