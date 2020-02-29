import pygame
from pygame.locals import *
from Board import Board
from Const import Const

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((Const.WinLength, Const.WinHeight))
pygame.display.set_caption(Const.ProgramName)

background = pygame.image.load("ImageSources/Board.bmp")
fpsClock = pygame.time.Clock()

board = Board()

inProgress = True
while inProgress:
    board.Play(surface, background)
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
    pygame.display.update()
    fpsClock.tick(Const.FPS)
pygame.quit()
