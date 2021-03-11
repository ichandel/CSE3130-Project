"""
title: ball
author: Ishaan Chandel
date-created: 2021-03-11
"""

from mySprite import MySprite
from loader import Colour
import pygame


class Ball(MySprite):

    def __init__(self):
        super().__init__()
        self.WIDTH = 20
        self.HEIGHT = 20
        self.COLOUR = Colour.WHITE
        self.X = 50
        self.Y = 50
        self.POS = (self.X, self.Y)
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOUR)
        self.SPEED = 5
        self.DIR_X = 1
        self.DIR_Y = -1

    def bounce(self, SCREEN):
        self.X = self.X + self.DIR_X * self.SPEED
        self.Y = self.Y + self.DIR_Y * self.SPEED
        if self.X > SCREEN.getVirtualWidth() - self.getWidth():
            self.DIR_X = -1
        if self.X < 0:
            self.DIR_X = 1
        if self.Y > SCREEN.getVirtualHeight() - self.getHeight():
            self.DIR_Y = -1
        if self.Y < 0:
            self.DIR_Y = 1
        self.updatePOS()