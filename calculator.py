import numbers

__all__ = ["add", "subtract", "multiply", "divide"]

def _ensure_number(value, name):
    if not isinstance(value, numbers.Number):
        raise TypeError(f"{name} must be a numeric type, got {type(value).__name__}")

def add(a: numbers.Number, b: numbers.Number) -> numbers.Number:
    """Return the sum of a and b.

    Raises:
        TypeError: if either operand is not a numeric type.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b

def subtract(a: numbers.Number, b: numbers.Number) -> numbers.Number:
    """Return the difference a - b.

    Raises:
        TypeError: if either operand is not a numeric type.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b

def multiply(a: numbers.Number, b: numbers.Number) -> numbers.Number:
    """Return the product of a and b.

    Raises:
        TypeError: if either operand is not a numeric type.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b

def divide(a: numbers.Number, b: numbers.Number) -> numbers.Number:
    """Return the quotient a / b.

    Raises:
        TypeError: if either operand is not a numeric type.
        ValueError: if b is zero.
    """
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b