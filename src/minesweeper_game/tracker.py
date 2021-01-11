import pygame
from src.object import Object
from src import constant as c


class Tracker(Object):

    def __init__(self, screen, tile_size):
        self._screen = screen
        self._location = None
        self._prev_location = None
        self._tile_size = tile_size

    def update(self, location2, counter):
        if self._prev_location is None:
            self._prev_location = location2
        location1 = self._prev_location
        division = counter / c.DELAY
        coordinates = self.interpolate(location1, location2, division)
        self._location = tuple(int((coord + 0.5) * self._tile_size) for coord in coordinates)

    def render(self):
        radius = self._tile_size // 4
        if self._location:
            pygame.draw.circle(self._screen, c.BLACK, self._location, radius)

    def update_prev_location(self, prev_location):
        self._prev_location = prev_location

    @staticmethod
    def interpolate(coord1, coord2, division):
        pause_fraction = 0.9
        division = (1 + pause_fraction) * division - pause_fraction
        if division < 0:
            division = 0
        x1, y1 = coord1
        x2, y2 = coord2
        new_x = x1 + (x2 - x1) * division
        new_y = y1 + (y2 - y1) * division
        new_coord = (new_x, new_y)
        return new_coord
