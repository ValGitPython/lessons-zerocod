def compress_string(s):
    if not s:  # Проверка на пустую строку
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    # Проходим по строке начиная со второго символа
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    # Добавляем последний символ и его количество
    result.append(current_char + str(count))
    
    return "".join(result)

# Основной цикл программы
while True:
    # Получаем ввод от пользователя
    input_string = input("Введите строку для сжатия (или 'ext' для выхода): ")
    
    # Проверяем условие выхода
    if input_string.lower() == 'ext':
        print("Программа завершена!")
        break
    
    # Сжимаем строку и выводим результат
    compressed = compress_string(input_string)
    print(f"Результат сжатия: {compressed}")
