import pygame
from src.object import Object
import src.constant as c


class TileBorder(Object):

    def __init__(self, screen, x, y, size):
        super().__init__(screen)
        self._x = x
        self._y = y
        self._size = size
        self._colour = c.BLACK
        self._on = False
        self._next_tile = False

    def update(self):
        if self._next_tile:
            self._colour = c.ORANGE
        else:
            self._colour = c.BLACK
        self._on = False
        self._next_tile = False

    def render(self):
        if self._on:
            border_thickness = 5
            x = self._x * self._size + border_thickness // 2
            y = self._y * self._size + border_thickness // 2
            size = self._size - border_thickness
            rect = (x, y, size, size)
            pygame.draw.rect(self._screen, self._colour, rect, border_thickness)

    def toggle(self, state):
        self._on = state

    def toggle_next_tile(self):
        self._next_tile = True
