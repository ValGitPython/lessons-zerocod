def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Демонстрация работы функции
print("Результат 10/2:", safe_divide(10, 2))
print("Результат 10/0:", safe_divide(10, 0))
print("Результат 15/3:", safe_divide(15, 3))
