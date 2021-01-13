import pygame
from src.object import Object
from src import constant as c


class Tracker(Object):

    def __init__(self, screen, tile_size):
        super().__init__(screen)
        self._location = None
        self._tile_size = tile_size
        self._prev_location = None
        self._next_location = None
        self._counter = 1

    def update(self):
        # Waits until a tile is clicked for tracker location to be declared
        if self._next_location:
            if self._prev_location is None:
                self._prev_location = self._next_location

            division = self._counter / c.DELAY

            # Time dependent smooth transitioning between tiles of the tracker
            coordinates = self.interpolate(self._prev_location, self._next_location, division)

            # Shift tracker location to the centre of the tile rather than the top left corner
            self._location = tuple(int((coord + 0.5) * self._tile_size) for coord in coordinates)

    def render(self):
        radius = self._tile_size // 4
        if self._location:
            pygame.draw.circle(self._screen, c.BLACK, self._location, radius)

    def update_prev_location(self, prev_location):
        self._prev_location = prev_location

    def update_next_location(self, next_location):
        self._next_location = next_location

    def update_counter(self, counter):
        self._counter = counter

    @staticmethod
    def interpolate(coord1, coord2, division):

        # Fraction of time the tracker is on the tile
        pause_fraction = 0.9
        division = (1 + pause_fraction) * division - pause_fraction
        if division < 0:
            division = 0

        # Line segment division
        x1, y1 = coord1
        x2, y2 = coord2
        new_x = x1 + (x2 - x1) * division
        new_y = y1 + (y2 - y1) * division
        new_coord = (new_x, new_y)
        return new_coord

