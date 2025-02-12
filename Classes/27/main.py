import os
import pandas as pd


def get_file_path():
    while True:
        file_path = input("Введите путь к файлу dz.csv: ").strip('"\'')  # Удаляем кавычки
        if os.path.exists(file_path):
            if os.path.basename(file_path) == 'dz.csv':
                return file_path
            else:
                print("Ошибка: Выбранный файл не является dz.csv. Пожалуйста, выберите правильный файл.")
        else:
            print("Ошибка: Указанный путь не существует. Пожалуйста, попробуйте снова.")


def calculate_average_salary(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'City' in df.columns and 'Salary' in df.columns:
            average_salary_by_city = df.groupby('City')['Salary'].mean()
            return average_salary_by_city
        else:
            print("Ошибка: В файле отсутствуют необходимые колонки 'City' или 'Salary'.")
            return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def main():
    file_path = get_file_path()
    average_salary_by_city = calculate_average_salary(file_path)

    if average_salary_by_city is not None:
        print("\nСредняя зарплата по городам:")
        for city, salary in average_salary_by_city.items():
            print(f"{city}: {salary:.2f}")  # Форматируем вывод до двух знаков после запятой


if __name__ == "__main__":
    main()