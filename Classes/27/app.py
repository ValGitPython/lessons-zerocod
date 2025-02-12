import pandas as pd
import os

def load_and_display_csv():
    # Запрос пути до CSV-файла у пользователя
    csv_path = input("Введите путь до CSV-файла (без кавычек): ").strip().strip('"')

    # Проверка существования файла
    if not os.path.isfile(csv_path):
        print("Файл не найден. Пожалуйста, проверьте путь и повторите попытку.")
        return

    # Загрузка данных из CSV-файла в DataFrame
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла: {e}")
        return

    # Запрос количества строк для вывода
    while True:
        num_rows_input = input("Введите количество строк для вывода: ").strip()
        if num_rows_input.isdigit():
            num_rows = int(num_rows_input)
            break
        else:
            print("Пожалуйста, введите целое число.")

    # Вывод запрашиваемых строк данных
    print(f"\nПервые {num_rows} строк данных:")
    print(df.head(num_rows))

    # Вывод информации о данных
    print("\nИнформация о данных:")
    df.info()

    # Вывод статистического описания данных
    print("\nСтатистическое описание данных:")
    print(df.describe())

# Запуск программы
load_and_display_csv()
