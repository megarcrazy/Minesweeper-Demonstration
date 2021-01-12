import pygame
from src.helper_objects.button import Button
from src.settings_window.settings_scene import Settings
import src.constant as c


class SettingsButton(Button):

    def __init__(self, screen):
        super().__init__(screen)
        self._x, self._y = c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT * 3 // 4
        self._scene_pointer = Settings(self._screen)
        self._text = "Settings"

        rect = self.set_rectangle()
        self._centre = rect[:2]
        self._rect = Button.centre_rectangle(rect)
        self._colour = c.TOMATO

    def update(self):
        if self.check_hover():
            self._colour = c.LIGHT_SALMON
        else:
            self._colour = c.TOMATO
        if self.check_on_click():
            return True
        return False
