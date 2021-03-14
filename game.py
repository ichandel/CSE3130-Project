"""
Title: Brickbreaker :)
Author: Ishaan Chandel
Date: 2021-03-08
"""

import pygame
from random import randrange
from window import Window
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
        """
        places all bricks for level 1
        """
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
        """
        places all bricks for level 2
        """
        STARTX = 0
        STARTY = 50
        for i in range(28):
            if STARTX < (self.WINDOW.getVirtualWidth() // 9) * 7:
                STARTX = STARTX + self.WINDOW.getVirtualWidth() // 9
            else:
                STARTX = self.WINDOW.getVirtualWidth() // 9
                STARTY = STARTY + 120
            NEWBRICK = Brick(STARTX, STARTY)
            self.BRICKS.append(NEWBRICK)

    def makeColoursHot(self):
        """
        changes bricks' colour to warmer colour temperatures
        This is an example of aggregation where each brick's colour is changed individually despite all of them being
        the same type of object and in the same array.
        """
        for i in range(len(self.BRICKS)):
            HOTS = randrange(1, 6)
            if HOTS == 1:
                self.BRICKS[i].COLOUR = Colour.INDIAN_RED
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif HOTS == 2:
                self.BRICKS[i].COLOUR = Colour.PINK
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif HOTS == 3:
                self.BRICKS[i].COLOUR = Colour.PASTEL_PINK
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif HOTS == 4:
                self.BRICKS[i].COLOUR = Colour.CORAL
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif HOTS == 5:
                self.BRICKS[i].COLOUR = Colour.PALE_VIOLET_RED
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)

    def makeColoursCold(self):
        """
        changes bricks' colour to colder colour temperatures
        """
        for i in range(len(self.BRICKS)):
            COLDS = randrange(1, 6)
            if COLDS == 1:
                self.BRICKS[i].COLOUR = Colour.MEDIUM_SPRING_GREEN
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif COLDS == 2:
                self.BRICKS[i].COLOUR = Colour.CORNFLOWER_BLUE
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif COLDS == 3:
                self.BRICKS[i].COLOUR = Colour.DARK_SLATE_BLUE
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif COLDS == 4:
                self.BRICKS[i].COLOUR = Colour.MEDIUM_AQUAMARINE
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)
            elif COLDS == 5:
                self.BRICKS[i].COLOUR = Colour.DARK_CYAN
                self.BRICKS[i].SCREEN.fill(self.BRICKS[i].COLOUR)


    def getPaddleBallCollision(self):
        """
        checks for collision between paddle and ball
        :return: boolean
        """
        if pygame.Rect.colliderect(self.PADDLE.getRect(), self.BALL.getRect()):
            return True
        else:
            return False

    def startScreen(self):
        """
        makes start screen for game
        """

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            # the follosing code creates, positions and blits on various text objects for user readability

            self.TITLE = Text("Welcome To Brickbreaker :)!")
            self.SUBTITLE = Text("Use the A and D keys to move your paddle.", FONTSIZE=20)
            self.SUBTITLE4 = Text("The ball progressively gets faster with each hit!", FONTSIZE=20)
            self.SUBTITLE5 = Text("Press enter to continue.", FONTSIZE=20)
            self.SUBTITLE6 = Text("Press ESC to exit.", FONTSIZE=20)
            self.SUBTITLE9 = Text("What colour paddle would you like?", FONTSIZE=20)
            self.OPT1 = Text("[1] Default: White", FONTSIZE=15)
            self.OPT2 = Text("[2]: Grey", FONTSIZE=15)
            self.OPT3 = Text("[3]: Red", FONTSIZE=15)
            self.OPT4 = Text("[4]: Green", FONTSIZE=15)
            self.OPT5 = Text("[5]: Magenta", FONTSIZE=15)
            self.TITLE.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE.getHeight()) // 2 - 100)
            self.SUBTITLE.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE.getHeight()) // 2 - 30)
            self.SUBTITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE4.getHeight()) // 2 + 0)
            self.SUBTITLE5.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE5.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE5.getHeight()) // 2 + 30)
            self.SUBTITLE6.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE6.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE6.getHeight()) // 2 + 60)
            self.SUBTITLE9.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE9.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE9.getHeight()) // 2 + 90)
            self.OPT1.setPOS((self.WINDOW.getVirtualWidth() - self.OPT1.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT1.getHeight()) // 2 + 115)
            self.OPT2.setPOS((self.WINDOW.getVirtualWidth() - self.OPT2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT2.getHeight()) // 2 + 140)
            self.OPT3.setPOS((self.WINDOW.getVirtualWidth() - self.OPT3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT3.getHeight()) // 2 + 165)
            self.OPT4.setPOS((self.WINDOW.getVirtualWidth() - self.OPT4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT4.getHeight()) // 2 + 190)
            self.OPT5.setPOS((self.WINDOW.getVirtualWidth() - self.OPT5.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT5.getHeight()) // 2 + 215)
            self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE.getScreen(), self.SUBTITLE.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE4.getScreen(), self.SUBTITLE4.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE5.getScreen(), self.SUBTITLE5.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE6.getScreen(), self.SUBTITLE6.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE9.getScreen(), self.SUBTITLE9.getPOS())
            self.WINDOW.getScreen().blit(self.OPT1.getScreen(), self.OPT1.getPOS())
            self.WINDOW.getScreen().blit(self.OPT2.getScreen(), self.OPT2.getPOS())
            self.WINDOW.getScreen().blit(self.OPT3.getScreen(), self.OPT3.getPOS())
            self.WINDOW.getScreen().blit(self.OPT4.getScreen(), self.OPT4.getPOS())
            self.WINDOW.getScreen().blit(self.OPT5.getScreen(), self.OPT5.getPOS())

            self.WINDOW.updateFrame()

            # processing

            # the following code allows the paddle object to change colour according to user needs

            if KEYPRESSES[pygame.K_1]:
                self.PADDLE.COLOUR = Colour.WHITE
                self.PADDLE.SCREEN.fill(self.PADDLE.COLOUR) # output
            if KEYPRESSES[pygame.K_2]:
                self.PADDLE.COLOUR = Colour.GREY
                self.PADDLE.SCREEN.fill(self.PADDLE.COLOUR)
            if KEYPRESSES[pygame.K_3]:
                self.PADDLE.COLOUR = Colour.RED
                self.PADDLE.SCREEN.fill(self.PADDLE.COLOUR)
            if KEYPRESSES[pygame.K_4]:
                self.PADDLE.COLOUR = Colour.GREEN
                self.PADDLE.SCREEN.fill(self.PADDLE.COLOUR)
            if KEYPRESSES[pygame.K_5]:
                self.PADDLE.COLOUR = Colour.MAGENTA
                self.PADDLE.SCREEN.fill(self.PADDLE.COLOUR)


            if KEYPRESSES[pygame.K_RETURN]: # this line runs the maing game once the user is ready
                self.runLvl1()
            if KEYPRESSES[pygame.K_ESCAPE]: # this exits the program when the user wishes to
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
    def pauseScreen(self): # screen between levels to allow for a break

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
            self.TITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE3.getHeight()) // 2 - 50)
            self.SUBTITLE7.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE7.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE7.getHeight()) // 2 + 20)
            self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
            self.WINDOW.getScreen().blit(self.TITLE3.getScreen(), self.TITLE3.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE7.getScreen(), self.SUBTITLE7.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runLvl2()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def winScreen(self): # screen displayed after completing level 2

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            self.TITLE4 = Text("Game Complete!")
            self.SUBTITLE8 = Text("Press enter to play again.", FONTSIZE=20)
            self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
            self.TITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE4.getHeight()) // 2 - 50)
            self.SUBTITLE8.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE8.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE8.getHeight()) // 2 + 20)
            self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
            self.WINDOW.getScreen().blit(self.TITLE4.getScreen(), self.TITLE4.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE8.getScreen(), self.SUBTITLE8.getPOS())
            self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
            self.WINDOW.updateFrame()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runLvl1()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def runLvl1(self):
        """
        contains code to create and run all of level 1 and its roles
        """

        self.placeBricksLvl1()
        self.makeColoursHot()
        self.SCORE = 0
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

            if self.getPaddleBallCollision() == True: # makes ball bounce off paddle
                self.BALL.DIR_Y = -1
                self.BALL.SPEED += 0.2 # speeds ball up to increase difficulty everytime ball hits paddle

            if len(self.BRICKS) > 0: # runs code for collisions as long as their are bricks on screen
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    if pygame.Rect.colliderect(self.BALL.getRect(), self.BRICKS[i].TOP): # checks for collision with top rect and so on
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
            elif len(self.BRICKS) <= 0 and self.SCORE == 24: # after all bricks have been hit and the score has reached 24 takes user to pause screen
                self.pauseScreen()



            if self.BALL.Y > self.WINDOW.getVirtualHeight() - self.BALL.getHeight(): # code that displays game over screen if the ball hits the bottom border
                for i in range(len(self.BRICKS) - 1, -1, -1):
                    self.BRICKS.pop(i)
                self.SCORE = 0
                self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                self.endScreen()

            """
            an example of encapsulation can be viewed here where the user only sees the basic objects that have been
            blit onto the screen but doesn't see the code that counts score and makes the ball bounce and pickup pace
            as well as see the code that randomizes the bricks' colours
            """

            self.WINDOW.clearScreen()
            for brick in self.BRICKS:
                self.WINDOW.getScreen().blit(brick.getScreen(), brick.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PADDLE.getScreen(), self.PADDLE.getPOS())
            self.WINDOW.getScreen().blit(self.BALL.getScreen(), self.BALL.getPOS())
            self.WINDOW.updateFrame()

    def runLvl2(self):
        """
        contains code to create and run all of level 2 and its roles
        """

        self.placeBricksLvl2()
        self.makeColoursCold()
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
            elif len(self.BRICKS) <= 0 and self.SCORE == 52:
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