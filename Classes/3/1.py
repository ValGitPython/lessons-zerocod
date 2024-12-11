def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

def calculator():
    print("Калькулятор")
    
    # Получаем числа с проверкой
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    
    # Показываем меню операций
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Целочисленное деление (//)")
    print("6. Остаток от деления (%)")
    print("7. Возведение в степень (**)")
    print("8. Показать все операции")
    
    while True:
        try:
            choice = int(input("\nВыберите операцию (1-8): "))
            if choice not in range(1, 9):
                print("Пожалуйста, выберите число от 1 до 8")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    
    # Выполняем выбранную операцию
    if choice == 1:
        print(f"Сложение: {num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"Вычитание: {num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"Умножение: {num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Деление: {num1} / {num2} = {num1 / num2}")
        else:
            print("Деление на ноль невозможно!")
    elif choice == 5:
        if num2 != 0:
            print(f"Целочисленное деление: {num1} // {num2} = {num1 // num2}")
        else:
            print("Деление на ноль невозможно!")
    elif choice == 6:
        if num2 != 0:
            print(f"Остаток от деления: {num1} % {num2} = {num1 % num2}")
        else:
            print("Деление на ноль невозможно!")
    elif choice == 7:
        print(f"Возведение в степень: {num1} ** {num2} = {num1 ** num2}")
    else:
        print(f"\nРезультаты всех операций с числами {num1} и {num2}:")
        print(f"Сложение: {num1} + {num2} = {num1 + num2}")
        print(f"Вычитание: {num1} - {num2} = {num1 - num2}")
        print(f"Умножение: {num1} * {num2} = {num1 * num2}")
        if num2 != 0:
            print(f"Деление: {num1} / {num2} = {num1 / num2}")
            print(f"Целочисленное деление: {num1} // {num2} = {num1 // num2}")
            print(f"Остаток от деления: {num1} % {num2} = {num1 % num2}")
        else:
            print("Деление на ноль невозможно!")
        print(f"Возведение в степень: {num1} ** {num2} = {num1 ** num2}")

    # Спрашиваем о продолжении
    while True:
        again = input("\nХотите выполнить еще вычисление? (да/нет): ").lower()
        if again in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'да' или 'нет'")
    
    if again == 'да':
        print("\n" + "="*50 + "\n")
        calculator()

# Запускаем калькулятор
calculator()
