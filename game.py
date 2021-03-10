"""
Title: Brickbreaker :)
Author: Ishaan Chandel
Date: 2021-03-08
"""

import pygame
from random import randrange
from window import Window
from imageSprite import ImageSprite
from loader import Image
from loader import Colour
from text import Text

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window()
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

            self.TITLE = Text("Welcome To Brickbreaker :)!")
            self.SUBTITLE = Text("Press ENTER to continue.")
            self.TITLE.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE.getHeight()) // 2 + 20)
            self.SUBTITLE.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE.getHeight()) // 2 + 20)
            self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE.getScreen(), self.SUBTITLE.getPOS())
            self.WINDOW.updateFrame()

    def run(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # Processing


            # Outputs
            self.WINDOW.clearScreen()
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
            for egg in self.EGGS:
                self.WINDOW.getScreen().blit(egg.getScreen(), egg.getPOS())
            for shrub in self.SHRUBS:
                self.WINDOW.getScreen().blit(shrub.getScreen(), shrub.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.TIME_TEXT.getScreen(), self.TIME_TEXT.getPOS())
            self.WINDOW.updateFrame()

        while self.TIME_LEFT <= 0:
            self.WINDOW.clearScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.END_TEXT = Text("Game End!")
            self.FINAL_SCORE = Text(f"Final Score: {self.SCORE}")
            self.END_TEXT.setPOS((self.WINDOW.getVirtualWidth() - self.END_TEXT.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.END_TEXT.getHeight()) // 2 - 20)
            self.FINAL_SCORE.setPOS((self.WINDOW.getVirtualWidth() - self.FINAL_SCORE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.FINAL_SCORE.getHeight()) // 2 + 20)
            self.WINDOW.getScreen().blit(self.END_TEXT.getScreen(), self.END_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.FINAL_SCORE.getScreen(), self.FINAL_SCORE.getPOS())
            self.WINDOW.updateFrame()



if __name__ == "__main__":
    GAME = Game()
    GAME.startScreen()
    GAME.run()