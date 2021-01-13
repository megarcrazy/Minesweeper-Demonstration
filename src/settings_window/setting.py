import pygame
from src.object import Object
import src.constant as c


class Setting(Object):

    def __init__(self, screen, x, y, colour, text):
        super().__init__(screen)
        self._x, self._y = x, y
        self._colour = colour
        self._text = text
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)

    def render(self):
        text = self._font.render(self._text, False, self._colour)
        self._screen.blit(text, (self._x, self._y))
