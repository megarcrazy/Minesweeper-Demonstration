import pygame
from src.settings_scene.command import Command
import src.constant as c


class SweepCommand(Command):

    def __init__(self, screen):
        super().__init__(screen)
        self._text = "HEYYYYY"
        self._x, self._y = 10, 10

    def render(self):
        text = self._font.render(self._text, False, (0, 0, 0))
        self._screen.blit(text, (self._x, self._y))
