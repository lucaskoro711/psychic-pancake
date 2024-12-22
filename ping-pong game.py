import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 4
ball_speed_y = 4

# Configurações das raquetes
paddle_width, paddle_height = 10, 100
player1 = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = 6

# Pontuações
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

# Relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Função para desenhar os elementos na tela
def draw_elements():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    text1 = font.render(str(score1), True, WHITE)
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text1, (WIDTH // 4, 20))
    screen.blit(text2, (WIDTH // 4 * 3, 20))

# Função para mover a bola
def move_ball():
    global ball_speed_x, ball_speed_y, score1, score2

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Rebater nas bordas superiores e inferiores
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Rebater nas raquetes
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Pontuação
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()

# Resetar a posição da bola
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controle das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    # Movimentar a bola
    move_ball()

    # Desenhar os elementos
    draw_elements()

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
