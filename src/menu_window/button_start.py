import pygame
from src.helper_objects.button import Button
from src.minesweeper_game.play import Play
from src import constant as c


class StartButton(Button):

    def __init__(self, screen):
        super().__init__(screen)
        self._x, self._y = c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 4
        self._text = "Start"
        self._scene_pointer = Play(self._screen)

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

    def set_rectangle(self):
        rect = (self._x, self._y, self._width, self._height)
        return rect

