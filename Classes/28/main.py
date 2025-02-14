import pandas as pd

# Создаем данные с оценками от 1 до 5
data = {
    'Ученик': ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Ольга', 'Дмитрий', 'Елена', 'Алексей', 'Татьяна'],
    'Математика': [5, 4, 3, 5, 4, 3, 4, 5, 4, 3],
    'Физика': [4, 3, 4, 5, 3, 4, 5, 4, 3, 4],
    'Химия': [5, 4, 5, 5, 4, 3, 4, 5, 4, 3],
    'Биология': [3, 4, 5, 4, 3, 4, 5, 4, 3, 4],
    'Литература': [4, 5, 4, 5, 4, 3, 4, 5, 4, 3]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# 1. Вывод первых строк
print("Первые строки DataFrame:")
print(df.head())

# 2. Средняя оценка по каждому предмету
average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

# 3. Медианная оценка по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# 4. Q1 и Q3 для математики
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 по математике: {Q1_math}")
print(f"Q3 по математике: {Q3_math}")
print(f"Межквартильный размах (IQR) по математике: {IQR_math}")

# 5. Стандартное отклонение
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)