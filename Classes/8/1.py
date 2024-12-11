def write_to_file():
    try:
        while True:
            text = input("Введите текст (не может быть пустым): ")
            if text.strip():  # Проверяем, что текст не пустой
                break
            print("Ошибка: текст не может быть пустым!")
            
        with open('user_data.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        print("✓ Текст успешно записан в файл user_data.txt")
        
    except IOError as e:
        print(f"Ошибка при работе с файлом: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    write_to_file()
