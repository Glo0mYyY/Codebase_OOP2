def divide(a, b):
    try:
        divsion = a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    return divsion