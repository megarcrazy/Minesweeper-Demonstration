import pygame
from src.settings_window.setting import Command
import src.constant as c


class SettingsTileBorderColour(Command):

    def __init__(self, screen, x, y):
        super().__init__(screen)
        self._text = "This is the colour of queued tile borders tiles."
        self._x, self._y = x, y
        self._colour = c.BLACK