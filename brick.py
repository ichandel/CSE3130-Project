"""
title: ball
author: Ishaan Chandel
date-created: 2021-03-11
"""

from mySprite import MySprite
from loader import Colour
import pygame

class Brick(MySprite):

    def __init__(self, X, Y):
        super().__init__()
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.COLOUR = Colour.GREY
        '''self.TOP = pygame.Rect(self.X, self.Y)
        self.LEFT = pygame.Rect(self.X, self.Y)
        self.RIGHT = pygame.Rect(self.X, self.Y)
        self.BOTTOM = pygame.Rect(self.X, self.Y)'''
        self.WIDTH = 150
        self.HEIGHT = 100
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOUR)
