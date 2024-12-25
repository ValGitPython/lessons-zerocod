import pygame
import random

# Определяем некоторые константы
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPAWN_RATE = 30  # Меньше = чаще
PLAYER_SPEED = 5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Ограничиваем движение игрока в пределах экрана
        self.rect.x = max(0, min(WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_SIZE, self.rect.y))


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)

    def move(self):
        self.rect.y += 5  # Скорость движения врага

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.rect.y = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Выживание")
    clock = pygame.time.Clock()

    player = Player()
    enemies = []
    score = 0
    running = True
    spawn_counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Движение игрока
        player.move()

        # Спавн врагов
        spawn_counter += 1
        if spawn_counter >= ENEMY_SPAWN_RATE:
            enemies.append(Enemy())
            spawn_counter = 0

        # Движение врагов
        for enemy in enemies:
            enemy.move()
            # Если враг выходит за пределы экрана, сбрасываем его
            if enemy.rect.top > HEIGHT:
                enemies.remove(enemy)
                score += 1  # Увеличиваем счет

        # Проверка на столкновение
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                running = False  # Конец игры при столкновении

        # Отрисовка
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player.rect)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy.rect)

        # Отображение счета
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Счет: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
