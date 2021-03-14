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
from brick import Brick

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window(WIDTH=1920, HEIGHT=1080, FPS=60)
        self.WINDOW.setBackgroundColor(Colour.BLACK)
        self.PADDLE = Paddle()
        self.BALL = Ball()
        self.BRICKS = []
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"Score: {self.SCORE}", FONTSIZE=30)

    def placeBricksLvl1(self):
        STARTX = 0
        STARTY = 50
        for i in range(24):
            if STARTX < (self.WINDOW.getVirtualWidth() // 10) * 8:
                STARTX = STARTX + self.WINDOW.getVirtualWidth() // 10
            else:
                STARTX = self.WINDOW.getVirtualWidth() // 10
                STARTY = STARTY + 120
            NEWBRICK = Brick(STARTX, STARTY)
            self.BRICKS.append(NEWBRICK)

    def placeBricksLvl2(self):
        STARTX = self.WINDOW.getVirtualWidth() // 10
        STARTY = 50
        for i in range(28):
            if STARTX < (self.WINDOW.getVirtualWidth() // 10) * 8:
                STARTX = STARTX + self.WINDOW.getVirtualWidth() // 10
            else:
                STARTX = self.WINDOW.getVirtualWidth() // 10
                STARTY = STARTY + 120
            NEWBRICK = Brick(STARTX, STARTY)
            self.BRICKS.append(NEWBRICK)

    def makeColoursHot(self):
        for i in range(len(self.BRICKS)):
            HOTS = randrange(5)

    def getPaddleBallCollision(self):
        if pygame.Rect.colliderect(self.PADDLE.getRect(), self.BALL.getRect()):
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
            self.SUBTITLE = Text("Use the A and D keys to move your paddle.", FONTSIZE=20)
            self.SUBTITLE4 = Text("The ball progressively gets faster with each hit!", FONTSIZE=20)
            self.SUBTITLE5 = Text("Press enter to continue.", FONTSIZE=20)
            self.SUBTITLE6 = Text("Press ESC to exit.", FONTSIZE=20)
            self.TITLE.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE.getHeight()) // 2 - 50)
            self.SUBTITLE.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE.getHeight()) // 2 + 20)
            self.SUBTITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE4.getHeight()) // 2 + 50)
            self.SUBTITLE5.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE5.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE5.getHeight()) // 2 + 80)
            self.SUBTITLE6.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE6.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE6.getHeight()) // 2 + 110)
            self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE.getScreen(), self.SUBTITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE4.getScreen(), self.SUBTITLE4.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE5.getScreen(), self.SUBTITLE5.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE6.getScreen(), self.SUBTITLE6.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runLvl1()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def endScreen(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            self.TITLE2 = Text("Game Over!")
            self.SUBTITLE2 = Text("Press enter to play again.", FONTSIZE=20)
            self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
            self.TITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE2.getHeight()) // 2 - 50)
            self.SUBTITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE2.getHeight()) // 2 + 20)
            self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
            self.WINDOW.getScreen().blit(self.TITLE2.getScreen(), self.TITLE2.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE2.getScreen(), self.SUBTITLE2.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runLvl1()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()
    def pauseScreen(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            self.TITLE3 = Text("Level One Complete!")
            self.SUBTITLE7 = Text("Press enter to continue to Level 2.", FONTSIZE=20)
            self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
            self.TITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE2.getHeight()) // 2 - 50)
            self.SUBTITLE7.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE7.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE7.getHeight()) // 2 + 20)
            self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
            self.WINDOW.getScreen().blit(self.TITLE2.getScreen(), self.TITLE2.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE7.getScreen(), self.SUBTITLE7.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runLvl2()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def winScreen(self):

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            self.TITLE3 = Text("Game Complete!")
            self.SUBTITLE7 = Text("Press enter to return to the Start Screen.", FONTSIZE=20)
            self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
            self.TITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE2.getHeight()) // 2 - 50)
            self.SUBTITLE7.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE7.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE7.getHeight()) // 2 + 20)
            self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
            self.WINDOW.getScreen().blit(self.TITLE2.getScreen(), self.TITLE2.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE7.getScreen(), self.SUBTITLE7.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.startScreen()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def runLvl1(self):

        self.placeBricksLvl1()
        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
        self.BALL.SPEED = 5

        self.PADDLE.setPOS((self.WINDOW.getVirtualWidth() - self.PADDLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - (self.WINDOW.getVirtualHeight() // 8)))
        self.BALL.setPOS((self.WINDOW.getVirtualWidth() - self.BALL.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - (self.WINDOW.getVirtualHeight() // 8) * 2))
        for brick in self.BRICKS:
            brick.setPOS(brick.X, brick.Y)

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Processing

            KEYPRESSES = pygame.key.get_pressed()

            self.PADDLE.adMoveChkBounds(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
            self.BALL.bounce(self.WINDOW)

            if self.getPaddleBallCollision() == True:
                self.BALL.DIR_Y = -1
                self.BALL.SPEED += 0.2

            if len(self.BRICKS) > 0:
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    if pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].TOP):
                        self.BALL.DIR_Y = -1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    elif pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].BOTTOM):
                        self.BALL.DIR_Y = 1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    if pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].LEFT):
                        self.BALL.DIR_X = -1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    elif pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].RIGHT):
                        self.BALL.DIR_X = 1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
            elif len(self.BRICKS) <= 0 and self.SCORE == 24:
                self.pauseScreen()



            if self.BALL.Y > self.WINDOW.getVirtualHeight() - self.BALL.getHeight():
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    self.BRICKS.pop(i)
                self.SCORE = 0
                self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                self.endScreen()

            self.WINDOW.clearScreen()
            for brick in self.BRICKS:
                self.WINDOW.getScreen().blit(brick.getScreen(), brick.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PADDLE.getScreen(), self.PADDLE.getPOS())
            self.WINDOW.getScreen().blit(self.BALL.getScreen(), self.BALL.getPOS())
            self.WINDOW.updateFrame()

    def runLvl2(self):

        for i in range(len(self.BRICKS)):
            self.BRICKS[i].COLOUR = Colour.BLUE
            self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)

        self.placeBricksLvl2()
        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
        self.BALL.SPEED = 5

        self.PADDLE.setPOS((self.WINDOW.getVirtualWidth() - self.PADDLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - (self.WINDOW.getVirtualHeight() // 8)))
        self.BALL.setPOS((self.WINDOW.getVirtualWidth() - self.BALL.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - (self.WINDOW.getVirtualHeight() // 8) * 2))
        for brick in self.BRICKS:
            brick.setPOS(brick.X, brick.Y)

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Processing

            KEYPRESSES = pygame.key.get_pressed()

            self.PADDLE.adMoveChkBounds(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
            self.BALL.bounce(self.WINDOW)

            if self.getPaddleBallCollision() == True:
                self.BALL.DIR_Y = -1
                self.BALL.SPEED += 0.2

            if len(self.BRICKS) > 0:
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    if pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].TOP):
                        self.BALL.DIR_Y = -1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    elif pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].BOTTOM):
                        self.BALL.DIR_Y = 1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    if pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].LEFT):
                        self.BALL.DIR_X = -1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
                    elif pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].RIGHT):
                        self.BALL.DIR_X = 1
                        self.BRICKS.pop(i)
                        self.SCORE += 1
                        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                        break
            elif len(self.BRICKS) <= 0 and self.SCORE == 24:
                self.winScreen()


            if self.BALL.Y > self.WINDOW.getVirtualHeight() - self.BALL.getHeight():
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    self.BRICKS.pop(i)
                self.SCORE = 0
                self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                self.endScreen()

            self.WINDOW.clearScreen()
            for brick in self.BRICKS:
                self.WINDOW.getScreen().blit(brick.getScreen(), brick.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PADDLE.getScreen(), self.PADDLE.getPOS())
            self.WINDOW.getScreen().blit(self.BALL.getScreen(), self.BALL.getPOS())
            self.WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = Game()
    GAME.startScreen()