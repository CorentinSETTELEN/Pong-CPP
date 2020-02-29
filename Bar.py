import pygame


class Bar:

    length = 10
    height = 60
    speed = 4

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, Bar.length, Bar.height)

    def MoveUp(self):
        if self.rect.y > 15:
            self.rect.y -= Bar.speed

    def MoveDown(self):
        if self.rect.y < 585 - Bar.height:
            self.rect.y += Bar.speed
