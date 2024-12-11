def sum_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Аргументы должны быть целыми числами")
    if start > end:
        raise ValueError("Начальное значение должно быть меньше или равно конечному")
    return sum(range(start, end + 1))

def main():
    while True:
        try:
            start = int(input("Введите начальное значение: "))
            end = int(input("Введите конечное значение: "))
            result = sum_range(start, end)
            print(f"Сумма чисел от {start} до {end}: {result}")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()