import json

animal_list = []
admin_list = []

class Animal:
    def __init__(self, class_animal, name, age, species, colors):
        self.class_animal = class_animal
        self.name = name
        self.age = age
        self.species = species
        self.colors = colors
        self.sounds = None  # Инициализация sounds
        self.meals = None   # Инициализация meals
        animal_list.append(self)

    def make_sound(self, sounds):
        self.sounds = sounds
        return self.sounds

    def eat(self, meals):
        self.meals = meals
        return self.meals

    def info(self):
        return {
            "class": self.class_animal,
            "name": self.name,
            "age": self.age,
            "species": self.species,
            "colors": self.colors,
            "sounds": self.sounds,
            "meals": self.meals,
        }

class Bird(Animal):
    def __init__(self, name, age, species, colors):
        super().__init__("птицы", name, age, species, colors)

class Mammal(Animal):
    def __init__(self, name, age, species, colors):
        super().__init__("животные", name, age, species, colors)

class Reptile(Animal):
    def __init__(self, name, age, species, colors):
        super().__init__("рептилии", name, age, species, colors)

class Admin:
    def __init__(self, class_admin, name, age):
        self.class_admin = class_admin
        self.name = name
        self.age = age
        admin_list.append(self)

    def info(self):
        return {
            "class": self.class_admin,
            "name": self.name,
            "age": self.age,
        }

class ZooKeeper(Admin):
    def __init__(self, name, age):
        super().__init__("работник зоопарка", name, age)

class Veterinarian(Admin):
    def __init__(self, name, age):
        super().__init__("ветеринар", name, age)

class Administrator(Admin):
    def __init__(self, name, age):
        super().__init__("администратор", name, age)

def save_data(filename="zoo_data.json"):
    data = {
        "animals": [animal.info() for animal in animal_list],
        "admins": [admin.info() for admin in admin_list],
    }
    with open(filename, "w") as f:
        json.dump(data, f)

def load_data(filename="zoo_data.json"):
    global animal_list, admin_list
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        animal_list = [Animal(animal['class'], animal['name'], animal['age'], animal['species'], animal['colors'])
                       for animal in data["animals"]]
        admin_list = [Admin(admin['class'], admin['name'], admin['age']) for admin in data["admins"]]
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка при чтении файла JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def add_animal(class_animal, name, age, species, colors):
    try:
        if class_animal.lower() == "птицы":
            Bird(name, age, species, colors)
        elif class_animal.lower() == "животные":
            Mammal(name, age, species, colors)
        elif class_animal.lower() == "рептилии":
            Reptile(name, age, species, colors)
        else:
            raise ValueError("Недопустимый класс животного.")
    except Exception as e:
        print(f"Не удалось добавить животное: {e}")

def remove_animal(name):
    global animal_list
    animal_list = [animal for animal in animal_list if animal.name != name]

def add_admin(class_admin, name, age):
    try:
        if class_admin == "работник зоопарка":
            ZooKeeper(name, age)
        elif class_admin == "ветеринар":
            Veterinarian(name, age)
        elif class_admin == "администратор":
            Administrator(name, age)
        else:
            raise ValueError("Недопустимый класс администратора.")
    except Exception as e:
        print(f"Не удалось добавить сотрудника: {e}")

def remove_admin(name):
    global admin_list
    admin_list = [admin for admin in admin_list if admin.name != name]

def display_animals():
    print("Список животных:")
    for animal in animal_list:
        print(f"- {animal.name}, Класс: {animal.class_animal}, Возраст: {animal.age}, Вид: {animal.species}, Окрас: {animal.colors}")

def display_admins():
    print("Список сотрудников:")
    for admin in admin_list:
        print(f"- {admin.name}, Должность: {admin.class_admin}, Возраст: {admin.age}")

# Пример использования
if __name__ == "__main__":
    load_data()  # Загрузка данных из файла, если он существует

    while True:
        print("\nВыберите действие:")
        print("1. Добавить животное")
        print("2. Удалить животное")
        print("3. Добавить сотрудника")
        print("4. Удалить сотрудника")
        print("5. Показать всех животных")
        print("6. Показать всех сотрудников")
        print("7. Сохранить данные")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            class_animal = input("Введите класс животного (птицы, животные, рептилии): ")
            name = input("Введите имя животного: ")
            age = input("Введите возраст животного: ")
            species = input("Введите вид животного: ")
            colors = input("Введите окрас животного: ")
            add_animal(class_animal, name, age, species, colors)

        elif choice == "2":
            name = input("Введите имя животного для удаления: ")
            remove_animal(name)

        elif choice == "3":
            class_admin = input("Введите класс сотрудника (работник зоопарка, ветеринар, администратор): ")
            name = input("Введите имя сотрудника: ")
            age = input("Введите возраст сотрудника: ")
            add_admin(class_admin, name, age)

        elif choice == "4":
            name = input("Введите имя сотрудника для удаления: ")
            remove_admin(name)

        elif choice == "5":
            display_animals()

        elif choice == "6":
            display_admins()

        elif choice == "7":
            save_data()
            print("Данные сохранены.")

        elif choice == "8":
            print("Выход...")
            break

        else:
            print("Некорректный ввод, попробуйте снова.")
