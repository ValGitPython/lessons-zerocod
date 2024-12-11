numbers = []  # создаем пустой список

# добавляем 3 элемента
numbers.append(5)
numbers.append(8)
numbers.append(3)

# вставляем 2 элемента в начало
numbers.insert(0, 10)
numbers.insert(0, 7)

# сортируем по убыванию
numbers.sort(reverse=True)

print(f"Отсортированный список: {numbers}")
