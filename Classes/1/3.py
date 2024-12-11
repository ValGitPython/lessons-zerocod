def caesar_cipher(text, shift, action='encrypt'):
    # Русский и английский алфавиты
    en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    if not text:
        raise ValueError("Текст не может быть пустым")
    
    # Если дешифруем, меняем направление сдвига
    if action == 'decrypt':
        shift = -shift
    
    result = ''
    
    for char in text:
        # Определяем, какой алфавит использовать
        if char.lower() in en_alphabet:
            alphabet = en_alphabet
        elif char.lower() in ru_alphabet:
            alphabet = ru_alphabet
        else:
            # Если символ не из алфавита, оставляем без изменений
            result += char
            continue
        
        # Определяем регистр символа
        is_upper = char.isupper()
        char = char.lower()
        
        # Находим позицию символа в алфавите
        char_index = alphabet.find(char)
        
        # Выполняем сдвиг с учетом размера алфавита
        new_index = (char_index + shift) % len(alphabet)
        new_char = alphabet[new_index]
        
        # Сохраняем исходный регистр
        if is_upper:
            new_char = new_char.upper()
            
        result += new_char
        
    return result

def get_valid_shift():
    """Получение корректного значения сдвига"""
    while True:
        try:
            shift = input("Введите сдвиг (целое число): ").strip()
            if not shift:
                print("Ошибка: значение не может быть пустым")
                continue
            shift = int(shift)
            return shift
        except ValueError:
            print("Ошибка: введите корректное целое число")

def get_valid_text():
    """Получение корректного текста"""
    while True:
        text = input("Введите текст: ").strip()
        if not text:
            print("Ошибка: текст не может быть пустым")
            continue
        return text

def get_valid_choice():
    """Получение корректного выбора действия"""
    valid_choices = {'1', '2', '3'}
    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if not choice:
            print("Ошибка: необходимо сделать выбор")
            continue
        if choice not in valid_choices:
            print("Ошибка: выберите 1, 2 или 3")
            continue
        return choice

def main():
    print("\nПрограмма шифрования методом Цезаря")
    print("=====================================")
    
    while True:
        try:
            print("\nВыберите действие:")
            print("1. Зашифровать текст")
            print("2. Расшифровать текст")
            print("3. Выйти")
            
            choice = get_valid_choice()
            
            if choice == '3':
                print("\nПрограмма завершена!")
                break
            
            text = get_valid_text()
            shift = get_valid_shift()
            
            action = 'encrypt' if choice == '1' else 'decrypt'
            
            try:
                result = caesar_cipher(text, shift, action)
                print("\nРезультат:")
                print(result)
            except ValueError as e:
                print(f"Ошибка при обработке текста: {e}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"\nПроизошла непредвиденная ошибка: {e}")
            print("Попробуйте снова")

if __name__ == "__main__":
    main()
