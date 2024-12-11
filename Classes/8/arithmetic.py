def validate_numbers(*args):
    """Проверяет, являются ли аргументы числами"""
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Аргумент {arg} должен быть числом")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Ошибка: деление на ноль невозможно")
    return a / b
