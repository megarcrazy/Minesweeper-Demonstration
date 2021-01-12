import pygame
from src.object import Object
import src.constant as c


class Command(Object):

    def __init__(self, screen):
        super().__init__(screen)
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)
        self._x, self._y = None, None
        self._text = None
        self._colour = None

    def render(self):
        text = self._font.render(self._text, False, self._colour)
        self._screen.blit(text, (self._x, self._y))
