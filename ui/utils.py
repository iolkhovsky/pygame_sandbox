import pygame


def rot_center(image, angle):
    center = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)

    return rotated_image, new_rect
