def is_numeric(value):
    """
    Check if a value is a valid numeric type (integer, float, or string representation of a number).
    
    This function validates whether the input can be considered a valid number for 
    mathematical operations. It accepts integers, floats, and string representations
    of numbers (including scientific notation).
    
    Args:
        value: The value to check for numeric validity. Can be of any type.
        
    Returns:
        bool: True if the value is a valid number (int, float, or numeric string),
              False otherwise.
              
    Examples:
        >>> is_numeric(42)
        True
        >>> is_numeric(3.14)
        True
        >>> is_numeric("123")
        True
        >>> is_numeric("45.67")
        True
        >>> is_numeric("1.23e-4")
        True
        >>> is_numeric(None)
        False
        >>> is_numeric("abc")
        False
        >>> is_numeric([1, 2, 3])
        False
    """
    # Handle None explicitly
    if value is None:
        return False
    
    # Check if already int or float
    if isinstance(value, (int, float)):
        # Handle special float values
        if isinstance(value, float):
            return not (value != value or value == float('inf') or value == float('-inf'))
        return True
    
    # Check if string representation of a number
    if isinstance(value, str):
        # Remove leading/trailing whitespace
        value = value.strip()
        
        # Empty string is not numeric
        if not value:
            return False
            
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    # All other types are not numeric
    return False


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # ❌ No division by zero check!

