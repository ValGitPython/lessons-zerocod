import arithmetic

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число")

def test_arithmetic():
    try:
        print("\n=== Калькулятор ===")
        a = get_number("Введите первое число: ")
        b = get_number("Введите второе число: ")

        print(f"\nРезультаты операций:")
        print(f"✓ Сложение: {a} + {b} = {arithmetic.add(a, b)}")
        print(f"✓ Вычитание: {a} - {b} = {arithmetic.subtract(a, b)}")
        print(f"✓ Умножение: {a} * {b} = {arithmetic.multiply(a, b)}")
        try:
            result = arithmetic.divide(a, b)
            print(f"✓ Деление: {a} / {b} = {result}")
        except ValueError as e:
            print(f"❌ Деление: {e}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    test_arithmetic()