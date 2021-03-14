"""
title: paddle
author: Ishaan Chandel
date-created: 2021-03-11
"""

from mySprite import MySprite
from loader import Colour
import pygame

class Paddle(MySprite): # a child class from the parent (MySprite) class. Example of inheritance

    def __init__(self):
        super().__init__()
        self.WIDTH = 200
        self.HEIGHT = 10
        self.COLOUR = Colour.WHITE
        self.X = 50
        self.Y = 50
        self.POS = (self.X, self.Y)
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.SCREEN.fill(self.COLOUR)
        self.SPEED = 10

    def adMove(self, KEYPRESSES):
        """
        method for the horizontal movement of the paddle
        :param KEYPRESSES: array
        :return: none
        """
        if KEYPRESSES[pygame.K_a]:
            self.X = self.X - self.SPEED
        if KEYPRESSES[pygame.K_d]:
            self.X = self.X + self.SPEED

    def adMoveChkBounds(self, KEYPRESSES, MAXWIDTH, MAXHEIGHT, MINWIDTH=0, MINHEIGHT=0):
        """
        method to combine movement and stop at bounds
        :param KEYPRESSES: array
        :param MAXWIDTH: int
        :param MAXHEIGHT: int
        :param MINWIDTH: int
        :param MINHEIGHT: int
        :return: none
        """
        self.adMove(KEYPRESSES)
        self.checkBounds(MAXWIDTH, MAXHEIGHT, MINWIDTH, MINHEIGHT)
