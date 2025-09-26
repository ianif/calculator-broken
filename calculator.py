def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.

    Args:
        a: The number to be subtracted from.
        b: The number to subtract.

    Returns:
        The difference between the two numbers.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of the two numbers.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b