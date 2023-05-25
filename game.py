import pygame
import math

# Для начала инициализируем pygame
pygame.init()

# Дисплей приложения
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perfect Circle")

# Инициализируем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры круга
circle_radius = 100
circle_center = (width // 2, height // 2)

# Начальная позиция мыши
mouse_position = (0, 0)

# Цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Обновка позиции
            mouse_position = pygame.mouse.get_pos()

    # Очистка
    screen.fill(BLACK)

    # Начало рисования 
    pygame.draw.circle(screen, WHITE, circle_center, circle_radius, 1)

    # Рисунок юзера
    pygame.draw.circle(screen, WHITE, mouse_position, circle_radius, 1)

    # Средний distance круга
    dx = circle_center[0] - mouse_position[0]
    dy = circle_center[1] - mouse_position[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)
    mse = (distance - circle_radius) ** 2

    # Расчеты 
    perfection = max(0, 1 - (mse / (circle_radius ** 2)))

    # Изменение цвета по мере допускания ошибок
    if mse > 0:
        angle = math.atan2(dy, dx)
        offset_x = int(circle_radius * math.cos(angle))
        offset_y = int(circle_radius * math.sin(angle))
        mistake_pos = (circle_center[0] - offset_x, circle_center[1] - offset_y)
        pygame.draw.circle(screen, RED, mistake_pos, 5)

    # Резуольтаты
    font = pygame.font.Font(None, 36)
    text = font.render(f"Perfection: {perfection:.2%}", True, WHITE)
    screen.blit(text, (10, 10))

    # Обновление дисплея 
    pygame.display.flip()

# Quit the game
pygame.quit()
