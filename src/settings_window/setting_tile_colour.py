import pygame
from src.settings_window.setting import Command
import src.constant as c


class SettingsTileColour(Command):

    def __init__(self, screen, x, y):
        super().__init__(screen)
        self._text = "This is the colour of unrevealed tiles."
        self._x, self._y = x, y
        self._colour = c.DARK_SLATE_BLUE
