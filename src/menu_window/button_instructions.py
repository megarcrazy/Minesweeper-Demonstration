import pygame
from src.helper_objects.button import Button
from src.instructions_window.instructions_scene import Instructions
import src.constant as c


class InstructionsButton(Button):

    def __init__(self, screen):
        super().__init__(screen)
        self._x, self._y = c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2
        self._text = "Instructions"

        self._scene_pointer = Instructions(self._screen)
        rect = (self._x, self._y, self._width, self._height)
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
