"""
title: Text Class
"""

from loader import Colour
import pygame
from mySprite import MySprite

class Text(MySprite):

    def __init__(self, TEXT="HELLO WORLD", COLOUR=Colour.WHITE):
        super().__init__()
        self.TEXT = TEXT
        self.COLOUR = COLOUR
        self.FONT = pygame.font.SysFont("Times New Roman", 36)
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOUR)

    def setText(self, NEW_TEXT):
        self.TEXT = NEW_TEXT
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOUR)

if __name__ == "__main__":
    from window import Window
    import sys

    pygame.init()

    WINDOW = Window()
    TEXT1 = Text()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        WINDOW.getScreen().blit(TEXT1.getScreen(), TEXT1.getPOS())
        WINDOW.updateFrame()