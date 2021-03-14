"""
title: ball
author: Ishaan Chandel
date-created: 2021-03-11
"""

from mySprite import MySprite
from loader import Colour
import pygame

class Brick(MySprite): # a child class from the parent (MySprite) class. Example of inheritance

    def __init__(self, X, Y):
        """
        initializes the brick object
        :param X: int
        :param Y: int
        """
        super().__init__()
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.COLOUR = Colour.GREY
        self.TOP = pygame.Rect((self.X, self.Y), (150, 10))
        self.LEFT = pygame.Rect((self.X, self.Y), (10, 100))
        self.RIGHT = pygame.Rect((self.X + 150, self.Y), (10, 100))
        self.BOTTOM = pygame.Rect((self.X, self.Y + 100), (150, 10))
        self.WIDTH = 150
        self.HEIGHT = 100
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOUR)