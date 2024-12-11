import random

choices = ['камень', 'ножницы', 'бумага']
player_score = 0
computer_score = 0

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "ничья"
    elif (
        (player_choice == 'камень' and computer_choice == 'ножницы') or
        (player_choice == 'ножницы' and computer_choice == 'бумага') or
        (player_choice == 'бумага' and computer_choice == 'камень')
    ):
        return "игрок"
    else:
        return "компьютер"

print("Игра 'Камень, ножницы, бумага' до 3 побед")

while player_score < 3 and computer_score < 3:
    print(f"\nСчет - Игрок: {player_score}, Компьютер: {computer_score}")
    
    player_choice = input("Выберите (камень/ножницы/бумага): ").lower()
    if player_choice not in choices:
        print("Неверный выбор!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    if winner == "игрок":
        player_score += 1
        print("Вы выиграли раунд!")
    elif winner == "компьютер":
        computer_score += 1
        print("Компьютер выиграл раунд!")
    else:
        print("Ничья!")

print(f"\nИтоговый счет - Игрок: {player_score}, Компьютер: {computer_score}")
print("Победитель:", "игрок" if player_score > computer_score else "компьютер")
