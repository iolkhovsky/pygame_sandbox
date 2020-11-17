import pygame
import random

from boat_model import BoatModel

WIDTH = 800
HEIGHT = 600
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

boat = BoatModel(int(0.5 * WIDTH), init_y=int(0.5 * HEIGHT), init_angle=0)


boat_img = pygame.image.load("rsc/boat.png")
boat_img = pygame.transform.rotate(pygame.transform.scale(boat_img, (128, 72)), 0).convert_alpha()

imagerect = boat_img.get_rect()

boat_x, boat_y = boat.pos
angle = 0

keys = {"up": 0, "down": 0}

power = 0.0

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
            if event.key == pygame.K_UP:
                keys["up"] = 1
            if event.key == pygame.K_DOWN:
                keys["down"] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys["up"] = 0
            if event.key == pygame.K_DOWN:
                keys["down"] = 0
    # Обновление

    if keys["up"]:
        power = min(1.0, power + 0.1)
    if keys["down"]:
        power = max(-1.0, power - 0.1)

    boat.update(power)
    boat_x, boat_y = boat.pos
    # Рендеринг
    screen.fill(BLUE)
    imagerect.centerx = boat_x
    imagerect.centery = boat_y
    screen.blit(pygame.transform.rotate(boat_img, boat.angle), (imagerect.x, imagerect.y))

    bar_offset_x, bar_offset_y = 20, 20
    pygame.draw.rect(screen, (0, 0, 0),
                     (bar_offset_x, bar_offset_y, 10, 200))
    if power > 0:
        pygame.draw.rect(screen, (0, 255, 0),
                         (bar_offset_x, bar_offset_y + int((1. - abs(power)) * 100), 10, int(abs(power) * 100)))
    elif power < 0:
        pygame.draw.rect(screen, (255, 0, 0),
                         (bar_offset_x, bar_offset_y + 100, 10, int(abs(power) * 100)))
    pygame.display.flip()

pygame.quit()

