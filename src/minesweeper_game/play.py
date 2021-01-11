import pygame
from src.scene import Scene
from src.minesweeper_game.grid import Grid
from src import constant as c


class Play(Scene):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self._grid = None
        self.initialise()

    def initialise(self):
        self._grid = Grid(self._screen, c.SIZE, c.SIZE)

    def update(self):
        self._grid.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._grid.render()
        pygame.display.flip()
