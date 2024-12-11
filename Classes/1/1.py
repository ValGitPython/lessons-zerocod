def contains_three(number):
    # Преобразуем число в строку и проверяем наличие цифры 3
    return '3' in str(number)

# Считаем количество чисел с цифрой 3
count = sum(1 for i in range(1, 2025) if contains_three(i))

print(f"Количество чисел от 1 до 2024, содержащих цифру 3: {count}")
