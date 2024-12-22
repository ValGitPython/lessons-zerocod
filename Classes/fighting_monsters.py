from abc import ABC, abstractmethod
import random

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self) -> str:
        return "Боец стреляет из лука."

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def attack(self) -> str:
        if self.weapon:
            return self.weapon.attack()
        return "У бойца нет оружия!"

# Класс Monster
class Monster:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} остаётся на {self.health} здоровья.")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster) -> None:
    while monster.health > 0:
        print(fighter.attack())
        damage = random.randint(10, 30)  # Случайный урон для примера
        print(f"{monster.name} получает {damage} урона.")
        monster.take_damage(damage)

# Функция для выбора оружия
def choose_weapon() -> Weapon:
    weapons = {
        '1': Sword(),
        '2': Bow()
    }
    
    print("Выберите оружие:")
    print("1. Меч")
    print("2. Лук")
    
    choice = input("Введите номер оружия: ")
    return weapons.get(choice, None)

# Главная функция
def main():
    while True:
        fighter = Fighter("Воин")
        monster = Monster("Гоблин", 50)

        # Выбор оружия
        weapon = choose_weapon()
        if weapon:
            fighter.change_weapon(weapon)
            battle(fighter, monster)
        else:
            print("Неверный выбор оружия!")

        # Запрос на новый бой
        play_again = input("Хотите начать новый бой? (y/n): ")
        if play_again.lower() != 'y':
            print("Спасибо за игру!")
            break

# Пример использования
if __name__ == "__main__":
    main()
