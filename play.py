import pygame
from scene_manager import SceneManager
from minesweeper.grid import Grid
import constant as c


class Play(SceneManager):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self._grid = None
        self.initialise()

    def initialise(self):
        self._grid = Grid(self._screen, 10, 10)

    def update(self):
        self._grid.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._grid.render()
        pygame.display.flip()
