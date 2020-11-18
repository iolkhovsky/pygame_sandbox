import pygame

from models.boat_model import BoatModel
from ui.bar import VerticalBar, HorizontalBar
from ui.utils import rot_center

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
pygame.display.set_caption("Boat simulator")
clock = pygame.time.Clock()

boat = BoatModel(init_position=(int(0.5 * WIDTH), int(0.5 * HEIGHT)), init_azimuth=0)


boat_img = pygame.image.load("rsc/boat.png")
boat_img = pygame.transform.rotate(pygame.transform.scale(boat_img, (128, 72)), 0).convert_alpha()


angle = 0

keys = {"up": 0, "down": 0, "left": 0, "right": 0}

power = 0.0
steering_angle = 0.0

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
            if event.key == pygame.K_LEFT:
                keys["left"] = 1
            if event.key == pygame.K_RIGHT:
                keys["right"] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys["up"] = 0
            if event.key == pygame.K_DOWN:
                keys["down"] = 0
            if event.key == pygame.K_LEFT:
                keys["left"] = 0
            if event.key == pygame.K_RIGHT:
                keys["right"] = 0
    # Обновление

    if keys["up"]:
        power = min(1.0, power + 0.05)
    if keys["down"]:
        power = max(-1.0, power - 0.05)
    if keys["right"]:
        steering_angle = min(90.0, steering_angle + 5)
    if keys["left"]:
        steering_angle = max(-90, steering_angle - 5)

    (boat_x, boat_y), _, _, angle = boat.update(relative_power=power, steering= -1 * steering_angle, dt=1/FPS)
    # Рендеринг
    screen.fill(BLUE)
    cur_boat_img, boat_rect = rot_center(boat_img, -1 * angle)
    boat_rect.centerx, boat_rect.centery = boat_x, boat_y

    screen.blit(cur_boat_img, (boat_rect.x, boat_rect.y))

    power_bar = VerticalBar()
    bar = power_bar.get_bar(power * 100.)
    screen.blit(bar, (20, 20))
    angle_bar = HorizontalBar(min_value=-90, max_value=90)
    bar = angle_bar.get_bar(steering_angle)
    screen.blit(bar, (40, 20))
    pygame.display.flip()

pygame.quit()

