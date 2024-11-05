import math

def check_numeric(value):
    if not isinstance(value,(int, float)):
        raise TypeError("Input must be a numeric value.")

def convert_degrees_to_radians(degrees):
    return math.radians(degrees)

def sine(degrees):
    check_numeric(degrees)
    radians = convert_degrees_to_radians(degrees)
    return math.sin(radians)

def cosine(degrees):
    check_numeric(degrees)
    radians = convert_degrees_to_radians(degrees)
    return math.cos(radians)

def tan(degrees):
    check_numeric(degrees)
    radians = convert_degrees_to_radians(degrees)
    cos_value = math.cos(radians)
    if math.isclose(cos_value, 0.0, abs_tol=1e-9):
        raise ValueError("Tan undefined.")
    return math.tan(radians)

def sqrt(value):
    check_numeric(value)
    if value < 0:
        raise ValueError("Value is less than zero.")
    return math.sqrt(value)

def log(value, base=math.e):
    check_numeric(value)
    check_numeric(base)
    if value <= 0:
        raise ValueError("Input is non-positive.")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    return math.log(value, base)

def exp(value):
    check_numeric(value)
    return math.exp(value)

def asine(value):
    check_numeric(value)
    if value < -1 or value > 1:
        raise ValueError("Undefined for the given input.")
    return math.asin(value)

def acosine(value):
    check_numeric(value)
    if value < -1 or value > 1:
        raise ValueError("Undefined for the given input.")
    return math.acos(value)

def atan(value):
    check_numeric(value)
    return math.atan(value)

def sinh(value):
    check_numeric(value)
    return math.sinh(value)

def cosh(value):
    check_numeric(value)
    return math.cosh(value)

def tanh(value):
    check_numeric(value)
    return math.tanh(value)