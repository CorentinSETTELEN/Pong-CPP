import pygame
from pygame.locals import *

from Const import Const

pygame.init()
surface = pygame.display.set_mode((Const.WinLength, Const.WinHeight))
pygame.display.set_caption(Const.ProgramName)

background = pygame.image.load("ImageSources/Board.bmp")
assert isinstance(surface, pygame.Surface)
surface.blit(background, (0, 0))
pygame.draw.rect(surface, (255,255,255), (10,10,200,100))

inProgress = True
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
pygame.quit()
