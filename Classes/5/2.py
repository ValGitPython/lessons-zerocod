print("Простой калькулятор")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/' and b != 0:
    result = a / b
else:
    print("Ошибка! Неверная операция или деление на ноль")
    exit()

print(f"Результат: {result}")
