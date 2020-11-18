import pygame


class VerticalBar:

    def __init__(self, width=10, height=200, min_value=-100, max_value=100, color_p=(0, 255, 0), color_n=(255, 0, 0)):
        self._width = width
        self._height = height
        self._min = min_value
        self._max = max_value
        self._color_p = color_p
        self._color_n = color_n
        self._zero_pos = None
        if self._min < 0 < self._max:
            self._zero_pos = int(self._max * self._height / (self._max - self._min))

    def get_bar(self, value):
        surf = pygame.Surface((self._width, self._height))
        surf.fill((0, 0, 0))
        if self._zero_pos is not None:
            if value >= 0:
                level = int(self._height * value / (self._max - self._min))
                pygame.draw.rect(surf, self._color_p, (0, self._zero_pos - level, self._width, level))
            else:
                level = int(self._height * abs(value) / (self._max - self._min))
                pygame.draw.rect(surf, self._color_n, (0, self._zero_pos, self._width, level))
        else:
            level = int(self._height * (value - self._min) / (self._max - self._min))
            pygame.draw.rect(surf, self._color_p if value >= 0 else self._color_n, (0, self._height - level,
                                                                                    self._width, level))
        return surf


class HorizontalBar:

    def __init__(self, width=200, height=10, min_value=-100, max_value=100, color_p=(0, 255, 0), color_n=(255, 0, 0)):
        self._width = width
        self._height = height
        self._min = min_value
        self._max = max_value
        self._color_p = color_p
        self._color_n = color_n
        self._zero_pos = None
        if self._min < 0 < self._max:
            self._zero_pos = int(self._max * self._width / (self._max - self._min))

    def get_bar(self, value):
        surf = pygame.Surface((self._width, self._height))
        surf.fill((0, 0, 0))
        if self._zero_pos is not None:
            if value >= 0:
                level = int(self._width * value / (self._max - self._min))
                pygame.draw.rect(surf, self._color_p, (self._zero_pos, 0, level, self._height))
            else:
                level = int(self._width * abs(value) / (self._max - self._min))
                pygame.draw.rect(surf, self._color_n, (self._zero_pos - level, 0, level, self._height))
        else:
            level = int(self._width * (value - self._min) / (self._max - self._min))
            pygame.draw.rect(surf, self._color_p if value >= 0 else self._color_n, (self._width - level, 0,
                                                                                    level, self._height))
        return surf
