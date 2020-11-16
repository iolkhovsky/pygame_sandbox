import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


boat_img = pygame.image.load("rsc/boat.png")
boat_img = pygame.transform.scale(boat_img, (128, 72)).convert_alpha()
imagerect = boat_img.get_rect()

boat_x, boat_y = int(0.5 * WIDTH), int(0.5 * HEIGHT)
angle = 0

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boat_x -= 5
            if event.key == pygame.K_RIGHT:
                boat_x += 5
            if event.key == pygame.K_UP:
                boat_y -= 5
            if event.key == pygame.K_DOWN:
                boat_y += 5
            if event.key == pygame.K_q:
                angle -= 5
            if event.key == pygame.K_w:
                angle += 5
    # Обновление
    
    # Рендеринг
    screen.fill(BLUE)
    imagerect.centerx = boat_x
    imagerect.centery = boat_y
    screen.blit(pygame.transform.rotate(boat_img, angle), (imagerect.x, imagerect.y))
    pygame.display.flip()

pygame.quit()

