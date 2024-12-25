import pygame
import random

# Определим некоторые константы
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED


class Ball:
    def __init__(self):
        self.reset()

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Удар о верхнюю и нижнюю границы
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def reset(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = BALL_SPEED * random.choice((1, -1))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Пинг-Понг")
        self.clock = pygame.time.Clock()
        self.running = True
        self.mode = None
        self.paddle1 = Paddle(20, HEIGHT // 2 - 50)
        self.paddle2 = Paddle(WIDTH - 30, HEIGHT // 2 - 50)
        self.ball = Ball()

    def main_menu(self):
        while True:
            self.screen.fill(BLACK)
            font = pygame.font.Font(None, 74)
            title = font.render("Пинг-Понг", True, WHITE)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))

            font = pygame.font.Font(None, 36)
            player_vs_pc = font.render("Нажмите 1 для игры с компьютером", True, WHITE)
            player_vs_player = font.render("Нажмите 2 для игры с игроком", True, WHITE)
            self.screen.blit(player_vs_pc, (WIDTH // 2 - player_vs_pc.get_width() // 2, HEIGHT // 2))
            self.screen.blit(player_vs_player, (WIDTH // 2 - player_vs_player.get_width() // 2, HEIGHT // 2 + 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.mode = 'pc'
                        return
                    elif event.key == pygame.K_2:
                        self.mode = 'player'
                        return

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BLACK)
            self.paddle1.move(pygame.K_w, pygame.K_s)

            if self.mode == 'player':
                self.paddle2.move(pygame.K_UP, pygame.K_DOWN)
            else:  # Игра против компьютера
                self.computer_ai()

            # Коллизия мяча с ракетками
            if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
                self.ball.dx *= -1

            self.ball.move()

            # Сброс мяча, если он выходит за пределы экрана
            if self.ball.rect.left <= 0 or self.ball.rect.right >= WIDTH:
                self.ball.reset()

            # Отрисовка объектов на экране
            pygame.draw.rect(self.screen, WHITE, self.paddle1.rect)
            pygame.draw.rect(self.screen, WHITE, self.paddle2.rect)
            pygame.draw.ellipse(self.screen, WHITE, self.ball.rect)
            pygame.draw.aaline(self.screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

            pygame.display.flip()
            self.clock.tick(60)

    def computer_ai(self):
        # Простая логика управления компьютером
        if self.ball.rect.centery > self.paddle2.rect.centery:
            self.paddle2.rect.y += PADDLE_SPEED if self.paddle2.rect.bottom < HEIGHT else 0
        else:
            self.paddle2.rect.y -= PADDLE_SPEED if self.paddle2.rect.top > 0 else 0


if __name__ == "__main__":
    game = Game()
    game.main_menu()
    game.run()
    pygame.quit()
2