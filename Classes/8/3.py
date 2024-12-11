import random

def load_students(filename='students.txt'):
    """Загружает список учеников из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            students = [line.strip() for line in file if line.strip()]
        return students
    except FileNotFoundError:
        return None

def save_students(students, filename='students.txt'):
    """Сохраняет список учеников в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for student in students:
                file.write(f"{student}\n")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False

def select_random_students():
    # Пробуем загрузить существующий список
    students = load_students()
    
    if students is None:
        # Если файл не существует, создаем новый список
        print("Файл со списком учеников не найден. Создаём новый список.")
        students = []
        while True:
            student = input("Введите имя ученика (или 'готово' для завершения): ").strip()
            if student.lower() == 'готово':
                break
            if student:
                students.append(student)
            else:
                print("Имя не может быть пустым!")
        
        # Сохраняем список в файл
        if students:
            save_students(students)
    
    if len(students) < 5:
        return f"Ошибка: в списке должно быть минимум 5 учеников. Сейчас: {len(students)}"
    
    selected = random.sample(students, 5)
    return selected

if __name__ == "__main__":
    print("\n=== Программа выбора учеников ===")
    result = select_random_students()
    
    if isinstance(result, list):
        print("\nСегодня отвечают:")
        for i, student in enumerate(result, 1):
            print(f"{i}. {student}")
    else:
        print(result)

