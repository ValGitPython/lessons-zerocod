def get_integer():
    while True:
        try:
            user_input = input("Пожалуйста, введите целое число: ")
            number = int(user_input)
            print(f"Отлично! Вы ввели число: {number}")
            return number
        except ValueError:
            print("Невозможно преобразовать введенное значение в целое число")
            print("Попробуйте еще раз")

# Запуск программы
if __name__ == "__main__":
    get_integer()
