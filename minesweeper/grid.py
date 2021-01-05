import pygame
import random
from minesweeper.tile import Tile
from minesweeper.adjancent_index_list import AdjacentIndexList
from minesweeper.tracker import Tracker
import constant as c


class Grid:

    def __init__(self, screen, width, height):
        self._screen = screen
        self._width, self._height = width, height
        self._tile_grid = []
        self._tile_size = min(c.SCREEN_WIDTH, c.SCREEN_HEIGHT) // self._width
        self._font = pygame.font.SysFont('Comic Sans MS', 30)

        self._first_click = True
        self._queue = []
        self._counter = 1
        self._tracker = Tracker(self._screen, self._tile_size)
        self.initialise()

    def initialise(self):
        self.initialise_tiles()
        self.add_bombs()

    def initialise_tiles(self):
        for i in range(self._width):
            self._tile_grid.append([])
            for j in range(self._height):
                self._tile_grid[i].append(Tile(self._screen, i, j, self._tile_size, self._font))

    def add_bombs(self):
        self.reset_tiles()
        bombs_count = int(c.BOMB_PROPORTION * self._width * self._height)
        for _ in range(bombs_count):
            x = random.randint(0, self._width - 1)
            y = random.randint(0, self._height - 1)
            while self._tile_grid[x][y].is_bomb():
                x = random.randint(0, self._width - 1)
                y = random.randint(0, self._height - 1)
            self._tile_grid[x][y].insert_bomb()
            self.increment_surrounding_bombs_count(x, y)

    def reset_tiles(self):
        for row in self._tile_grid:
            for tile in row:
                tile.reset()

    def increment_surrounding_bombs_count(self, x, y):
        for adjacent in AdjacentIndexList.get_adjacent_index_list():
            adjacent_x = adjacent[0] + x
            adjacent_y = adjacent[1] + y
            if 0 <= adjacent_x < self._width and 0 <= adjacent_y < self._height:
                self._tile_grid[adjacent_x][adjacent_y].increment_adjacent_bombs_count()

    def update(self):
        self.update_tiles()
        self.user_mouse_input()
        self.sweep_queue()

    def render(self):
        for row in self._tile_grid:
            for tile in row:
                tile.render()
        if self._queue:
            self._tracker.render()

    def update_tiles(self):
        for i in range(len(self._tile_grid)):
            for j in range(len(self._tile_grid[0])):
                self._tile_grid[i][j].update()
                if (i, j) in self._queue:
                    self._tile_grid[i][j].toggle_on_border()
                if self._queue and self._queue[0] == (i, j):
                    self._tile_grid[i][j].change_colour(c.KHAKI)

    def user_mouse_input(self):
        mouse_position = pygame.mouse.get_pos()
        x = mouse_position[0] // self._tile_size
        y = mouse_position[1] // self._tile_size
        self._tile_grid[x][y].set_hover_is_true()

        clicked = pygame.mouse.get_pressed()[0]
        if clicked and not self._queue:
            self.sweep(x, y)

    def sweep(self, x, y):
        tile = self._tile_grid[x][y]
        if self._first_click:
            while tile.get_adjacent_bombs_count() != 0 or tile.is_bomb():
                self.add_bombs()
            self._first_click = False

        if not tile.is_revealed():
            tile.reveal()
            if tile.get_adjacent_bombs_count() == 0 and not tile.is_bomb():
                for adjacent in AdjacentIndexList.get_adjacent_index_list():
                    adjacent_x = adjacent[0] + x
                    adjacent_y = adjacent[1] + y
                    if 0 <= adjacent_x < self._width and 0 <= adjacent_y < self._height:
                        self._queue.append((adjacent_x, adjacent_y))

    def sweep_queue(self):
        if self._queue:
            if self.loop_delay():
                tile_x, tile_y = self._queue.pop(0)
                self._tracker.update_prev_location((tile_x, tile_y))
                self.sweep(tile_x, tile_y)
            if len(self._queue):
                self._tracker.update(self._queue[0], self._counter)

    def loop_delay(self):
        self._counter += 1
        if self._counter == c.DELAY:
            self._counter = 1
            return True

        return False
