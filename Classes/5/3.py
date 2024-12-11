days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Введите номер месяца (1-12): "))

if month in days_in_month:
    print(f"В этом месяце {days_in_month[month]} дней")
else:
    print("Ошибка! Введите число от 1 до 12")
