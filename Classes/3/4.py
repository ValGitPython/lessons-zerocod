def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Ошибка! Значение должно быть положительным числом.")
                continue
            return number
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

def calculate_area():
    print("Калькулятор площади прямоугольника")
    print("-" * 40)
    
    # Получаем размеры с проверкой
    length = get_positive_number("Введите длину прямоугольника (см): ")
    width = get_positive_number("Введите ширину прямоугольника (см): ")
    
    # Вычисляем площадь
    area = length * width
    perimeter = 2 * (length + width)
    
    # Выводим результаты
    print("\nРезультаты вычислений:")
    print(f"• Длина: {length:.2f} см")
    print(f"• Ширина: {width:.2f} см")
    print(f"• Площадь: {area:.2f} кв.см")
    print(f"• Периметр: {perimeter:.2f} см")
    
    # Спрашиваем о продолжении
    while True:
        again = input("\nХотите посчитать ещё раз? (да/нет): ").lower()
        if again in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'да' или 'нет'")
    
    if again == 'да':
        print("\n" + "=" * 40 + "\n")
        calculate_area()

if __name__ == "__main__":
    calculate_area()
