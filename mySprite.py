"""
title: Abstract Sprite Class
author: Ishaan Chandel
date-created: 2021-03-08
"""

import pygame


class MySprite:

    def __init__(self):
        self.WIDTH = 0
        self.HEIGHT = 0
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = None
        self.X = 0
        self.Y = 0
        self.POS = (self.X, self.Y)
        self.SPD = 5

    # Setters

    def setPOS(self, X, Y):
        self.X = X
        self.Y = Y
        self.updatePOS()

    def updatePOS(self):
        self.POS = (self.X, self.Y)

    def updateDimension(self):
        self.DIMENSION = (self.WIDTH, self.HEIGHT)

    # Getters

    def getScreen(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getWidth(self):
        return self.SCREEN.get_rect().width

    def getHeight(self):
        return self.SCREEN.get_rect().height

    def getRect(self):
        self.RECT = self.SCREEN.get_rect()
        self.RECT.x = self.X
        self.RECT.y = self.Y
        return self.RECT

    def checkBounds(self, MAXWIDTH, MAXHEIGHT, MINWIDTH=0, MINHEIGHT=0):
        if self.X > MAXWIDTH - self.getWidth():
            self.X = MAXWIDTH - self.getWidth()
        elif self.X < MINWIDTH:
            self.X = MINWIDTH

        if self.Y > MAXHEIGHT - self.getHeight():
            self.Y = MAXHEIGHT - self.getHeight()
        elif self.Y < MINHEIGHT:
            self.Y = MINHEIGHT

        self.updatePOS()