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

def get_yes_no(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ['да', 'нет']:
            return response == 'да'
        print("Пожалуйста, введите 'да' или 'нет'")

def update_exchange_rates(rates):
    print("\nТекущие курсы валют:")
    for currency, rate in rates.items():
        print(f"• {currency}: {rate:.2f} RUB")
    
    if get_yes_no("\nХотите изменить курсы валют? (да/нет): "):
        print("\nВведите новые курсы валют:")
        for currency in rates.keys():
            while True:
                try:
                    new_rate = float(input(f"Введите курс для {currency} (текущий: {rates[currency]:.2f}): "))
                    if new_rate <= 0:
                        print("Курс должен быть положительным числом!")
                        continue
                    rates[currency] = new_rate
                    break
                except ValueError:
                    print("Ошибка! Введите числовое значение.")
        print("\nКурсы валют успешно обновлены!")
    return rates

def main():
    print("Конвертер валют")
    print("-" * 40)
    
    # Начальные курсы валют
    exchange_rates = {
        "USD": 91.85,  # Курс доллара к рублю
        "EUR": 98.90,  # Курс евро к рублю
        "CNY": 12.75   # Курс юаня к рублю
    }
    
    # Обновление курсов валют
    exchange_rates = update_exchange_rates(exchange_rates)
    
    while True:
        # Получаем сумму от пользователя
        amount = get_positive_number("\nВведите сумму в рублях: ")
        
        print("\nРезультаты конвертации:")
        # Конвертируем и выводим результаты
        for currency, rate in exchange_rates.items():
            converted = amount / rate
            print(f"{amount:.2f} RUB = {converted:.2f} {currency}")
            
        print("\nОбратная конвертация (для справки):")
        for currency, rate in exchange_rates.items():
            print(f"1 {currency} = {rate:.2f} RUB")
        
        # Спрашиваем о продолжении
        if not get_yes_no("\nХотите конвертировать ещё одну сумму? (да/нет): "):
            break
        
        # Спрашиваем об изменении курсов для следующей конвертации
        exchange_rates = update_exchange_rates(exchange_rates)
    
    print("\nСпасибо за использование конвертера валют!")

if __name__ == "__main__":
    main()
