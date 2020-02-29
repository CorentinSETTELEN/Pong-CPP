import pygame

from DirectionEnum import DirectionEnum


class Ball:

    size = 10

    def __init__(self):
        self.speed = 5
        self.rect = pygame.Rect(300, 295, 10, 10)
        self.direction = DirectionEnum.UpRight

    def Movement(self):
        if self.direction == DirectionEnum.UpRight:
            self.rect.y -= self.speed
            self.rect.x += self.speed

        elif self.direction == DirectionEnum.UpLeft:
            self.rect.y -= self.speed
            self.rect.x -= self.speed

        elif self.direction == DirectionEnum.DownRight:
            self.rect.y += self.speed
            self.rect.x += self.speed

        elif self.direction == DirectionEnum.DownLeft:
            self.rect.y += self.speed
            self.rect.x -= self.speed
