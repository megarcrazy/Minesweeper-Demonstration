import pygame
from src.object import Object
import src.constant as c


class BackMessage(Object):

    def __init__(self, screen):
        self._screen = screen
        self._text = "Press 'r' to go back to the menu"
        self._x, self._y = c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT - 20
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)

    def render(self):
        text = self._font.render(self._text, False, (0, 0, 0))
        text_rect = text.get_rect(center=(self._x, self._y))
        self._screen.blit(text, text_rect)