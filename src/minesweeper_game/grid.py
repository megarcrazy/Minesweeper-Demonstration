import pygame
import random
from src.gameobject import GameObject
from src.minesweeper_game.tile import Tile
from src.minesweeper_game.adjancent_index_list import AdjacentIndexList
from src.minesweeper_game.tracker import Tracker
from src import constant as c


class Grid(GameObject):

    def __init__(self, screen, width, height):
        super().__init__(screen)
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

    # Chooses a random number in the range of the amount of the tiles and adds the bomb
    # to the respective tile.
    def add_bombs(self):
        self.reset_tiles()
        bombs_count = int(c.BOMB_PROPORTION * self._width * self._height)
        for _ in range(bombs_count):
            x = random.randint(0, self._width - 1)
            y = random.randint(0, self._height - 1)

            # If a bomb is already in the tile, find another tile to add the bomb.
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
        self._tracker.update()
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

                # Turns on the border for all tiles in the queue
                self._tile_grid[i][j].toggle_border((i, j) in self._queue)

                # The next tile is assigned to the first to be out of the queue
                if self._queue and self._queue[0] == (i, j):
                    self._tile_grid[i][j].toggle_next_tile()

    # Sweeps tile when the left mouse button is clicked on the tile
    # Activates when there is no sweeping in progress
    def user_mouse_input(self):
        mouse_position = pygame.mouse.get_pos()
        x = mouse_position[0] // self._tile_size
        y = mouse_position[1] // self._tile_size
        self._tile_grid[x][y].set_hover_is_true()

        clicked = pygame.mouse.get_pressed(3)[0]
        if clicked and not self._queue:
            self.sweep(x, y)

    # Reveal an unrevealed tile and append surrounding tiles in a queue if
    # they are not already checked. Like the real game, the first tile is always
    # safe and there are no surrounding adjacent bombs.
    def sweep(self, x, y):
        tile = self._tile_grid[x][y]
        if self._first_click:

            # Checks if the first clicked tile has adjacent bombs or is a bomb.
            # Resets all the bombs until the condition is false.
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
                        tile = self._tile_grid[adjacent_x][adjacent_y]
                        if (adjacent_x, adjacent_y) not in self._queue and not tile.is_revealed():
                            self._queue.append((adjacent_x, adjacent_y))

    def sweep_queue(self):
        if self._queue:
            if self.loop_delay():
                tile_x, tile_y = self._queue.pop(0)
                self._tracker.update_prev_location((tile_x, tile_y))
                self.sweep(tile_x, tile_y)
            if len(self._queue):
                self._tracker.update_next_location(self._queue[0])
                self._tracker.update_counter(self._counter)

    def loop_delay(self):
        self._counter += 1
        if self._counter == c.DELAY:
            self._counter = 1
            return True
        return False
