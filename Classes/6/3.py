def bank(a, years):
    if not isinstance(a, (int, float)) or not isinstance(years, int):
        raise ValueError("Сумма должна быть числом, а срок - целым числом лет")
    if a <= 0 or years <= 0:
        raise ValueError("Сумма вклада и срок должны быть положительными числами")
    
    amount = a
    for _ in range(years):
        amount += amount * 0.1
    return amount

def main():
    while True:
        try:
            initial_amount = float(input("Введите сумму вклада (руб.): "))
            years = int(input("Введите срок вклада (лет): "))
            result = bank(initial_amount, years)
            print(f"Итоговая сумма через {years} лет: {result:.2f} руб.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
