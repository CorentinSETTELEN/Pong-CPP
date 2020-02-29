import pygame
from pygame.constants import *

from Ball import Ball
from Const import Const
from DirectionEnum import DirectionEnum
from Player import Player


class Board:
    winScore = 9
    limitUpper = pygame.Rect(0, 0, Const.WinLength, 15)
    limitLower = pygame.Rect(0, Const.WinHeight - 15, Const.WinLength, 15)
    boardRect = pygame.Rect(0, 0, Const.WinLength, Const.WinHeight)

    def __init__(self):
        self.playerOne = Player(1)
        self.playerTwo = Player(2)
        self.ball = Ball()

    def Play(self, surface, background):
        if self.playerOne.score < Board.winScore and self.playerTwo.score < Board.winScore:
            if self.ball.rect.colliderect(Board.boardRect):
                self.BallMovement()
                self.GetInput(pygame.key.get_pressed())
                self.DrawElements(surface, background)
            else:
                if self.ball.direction == DirectionEnum.UpRight or self.ball.direction == DirectionEnum.DownRight:
                    self.playerOne.score += 1
                    self.ball.rect = pygame.Rect(500, 295, 10, 10)
                    self.ball.direction = DirectionEnum.UpLeft
                else:
                    self.playerTwo.score += 1
                    self.ball.rect = pygame.Rect(300, 295, 10, 10)
                    self.ball.direction = DirectionEnum.UpRight
        else:
            self.DrawElements(surface, background)
            self.DrawWinText(surface)

    def BallMovement(self):
        # collision with bars
        if self.ball.rect.colliderect(self.playerOne.bar.rect):
            self.ball.direction = DirectionEnum.UpRight if self.ball.direction == DirectionEnum.UpLeft else \
                DirectionEnum.DownRight
        if self.ball.rect.colliderect(self.playerTwo.bar.rect):
            self.ball.direction = DirectionEnum.UpLeft if self.ball.direction == DirectionEnum.UpRight else \
                DirectionEnum.DownLeft

        # collision with walls
        if self.ball.rect.colliderect(Board.limitUpper):
            self.ball.direction = DirectionEnum.DownLeft if self.ball.direction == DirectionEnum.UpLeft else \
                DirectionEnum.DownRight
        if self.ball.rect.colliderect(Board.limitLower):
            self.ball.direction = DirectionEnum.UpRight if self.ball.direction == DirectionEnum.DownRight else \
                DirectionEnum.UpLeft

        self.ball.Movement()
        pass

    def GetInput(self, keys):
        if keys[K_UP]:
            self.playerTwo.bar.MoveUp()
        if keys[K_DOWN]:
            self.playerTwo.bar.MoveDown()
        if keys[K_w]:       # because QWERTY mapping
            self.playerOne.bar.MoveUp()
        if keys[K_s]:
            self.playerOne.bar.MoveDown()

    def DrawElements(self, surface: pygame.Surface, background):
        surface.blit(background, (0, 0))

        # draw bars
        pygame.draw.rect(surface, Const.WHITE, self.playerOne.bar.rect)
        pygame.draw.rect(surface, Const.WHITE, self.playerTwo.bar.rect)

        # draw scores
        self.DrawScore(surface)

        # draw ball
        pygame.draw.rect(surface, Const.WHITE, self.ball.rect)

    def DrawScore(self, surface):
        fontObj = pygame.font.SysFont("consolas", 48)
        textSurface = fontObj.render(str(self.playerOne.score), True, Const.WHITE)
        textRect = textSurface.get_rect()
        textRect.topleft = (285, 25)
        surface.blit(textSurface, textRect)

        fontObj = pygame.font.SysFont("consolas", 48)
        textSurface = fontObj.render(str(self.playerTwo.score), True, Const.WHITE)
        textRect = textSurface.get_rect()
        textRect.topleft = (455, 25)
        surface.blit(textSurface, textRect)

    def DrawWinText(self, surface):
        fontObj = pygame.font.SysFont("consolas", 80)
        textSurface = fontObj.render("YOU WIN ", True, Const.WHITE)
        textRect = textSurface.get_rect()
        textRect.topleft = (240, 245)
        surface.blit(textSurface, textRect)
        pass
