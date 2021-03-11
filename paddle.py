"""
title: paddle
author: Ishaan Chandel
date-created: 2021-03-11
"""

from mySprite import MySprite
from loader import Colour
import pygame

class Paddle(MySprite):

    def __init__(self):
        super().__init__()
        self.WIDTH = 150
        self.HEIGHT = 10
        self.COLOUR = Colour.WHITE
        self.X = 50
        self.Y = 50
        self.POS = (self.X, self.Y)
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOUR)
        self.SPEED = 5

    def adMove(self, KEYPRESSES):
        if KEYPRESSES[pygame.K_a]:
            self.X = self.X + self.SPEED
        if KEYPRESSES[pygame.K_d]:
            self.X = self.X + self.SPEED
