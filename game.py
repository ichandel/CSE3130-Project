"""
Title: Brickbreaker :)
Author: Ishaan Chandel
Date: 2021-03-08
"""

import pygame
from random import randrange
from window import Window
from imageSprite import ImageSprite
from loader import Colour
from paddle import Paddle
from ball import Ball
from text import Text

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window(WIDTH=1920, HEIGHT=1080, FPS=60)
        self.WINDOW.setBackgroundColor(Colour.BLACK)
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"Score: {self.SCORE}")


    def placeItems(self):
        pass

    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            return True
        else:
            return False

    def startScreen(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            self.TITLE = Text("Welcome To Brickbreaker :)!")
            self.SUBTITLE = Text("Press enter to continue.", FONTSIZE=20)
            self.TITLE.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE.getHeight()) // 2 - 50)
            self.SUBTITLE.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE.getHeight()) // 2 + 20)
            self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE.getScreen(), self.SUBTITLE.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                return


    def run(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()

            PADDLE = Paddle()

            # Processing
            self.WINDOW.clearScreen()
            PADDLE.setPOS((self.WINDOW.getVirtualWidth() - PADDLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - (self.WINDOW.getVirtualHeight()//8)))

            self.WINDOW.getScreen().blit(PADDLE.getScreen(), PADDLE.getPOS())

            self.WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = Game()
    GAME.startScreen()
    GAME.run()