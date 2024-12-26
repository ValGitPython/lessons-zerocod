class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            self.show_health_status()
            if not self.computer.is_alive():
                break
            
            # Ход компьютера
            self.computer.attack(self.player)
            self.show_health_status()

        self.declare_winner()

    def show_health_status(self):
        print(f"{self.player.name} (Здоровье: {self.player.health}) vs {self.computer.name} (Здоровье: {self.computer.health})")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
