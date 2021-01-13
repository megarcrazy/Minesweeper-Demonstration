import pygame
from src.object import Object
from src.minesweeper_game.tile_border import TileBorder
from src import constant as c


class Tile(Object):

    def __init__(self, screen, x, y, size, font):
        super().__init__(screen)
        self._x, self._y = x, y
        self._size = size
        self._font = font

        self._colour = c.DARK_TURQUOISE
        self._border = TileBorder(screen, x, y, size)
        self._hover = False
        self._next_tile = False

        self._revealed = False
        self._bomb = False
        self._adjacent_bombs_count = 0

    def update(self):
        self._border.update()

        # Unrevealed tiles change colour when mouse hovers over them.
        # Tile colour changes again when revealed depending whether
        # it is a bomb or not.
        if not self._revealed:
            if self._hover:
                self._colour = c.HOVERED_TILE_COLOUR
            else:
                self._colour = c.UNREVEALED_TILE_COLOUR
        else:
            if self._bomb:
                self._colour = c.BOMB_TILE_COLOUR
            else:
                self._colour = c.REVEALED_TILE_COLOUR

        # Reset hover status
        self._hover = False

    def render(self):
        self.render_tile()
        self.render_tile_border()
        self.render_tile_text()

    def render_tile(self):
        x = self._x * self._size
        y = self._y * self._size
        rect = (x, y, self._size - 1, self._size - 1)
        pygame.draw.rect(self._screen, self._colour, rect)

    def render_tile_border(self):
        self._border.render()

    # Centres tile text to the centre of the tile. If tile is not a bomb,
    # it reveals information on how many adjacent tiles there are.
    def render_tile_text(self):
        if self._revealed and not self._bomb and self._adjacent_bombs_count != 0:
            text = self._font.render(str(self._adjacent_bombs_count), False, (0, 0, 0))
            x = int(self._size * (self._x + 0.5))
            y = int(self._size * (self._y + 0.5))
            text_rect = text.get_rect(center=(x, y))
            self._screen.blit(text, text_rect)

    def set_hover_is_true(self):
        self._hover = True

    def insert_bomb(self):
        self._bomb = True

    def is_bomb(self):
        return self._bomb

    def reset(self):
        self._adjacent_bombs_count = 0
        self._bomb = False

    def increment_adjacent_bombs_count(self):
        self._adjacent_bombs_count += 1

    def get_adjacent_bombs_count(self):
        return self._adjacent_bombs_count

    def is_revealed(self):
        return self._revealed

    def reveal(self):
        self._revealed = True

    def toggle_border(self, state):
        self._border.toggle(state)

    def toggle_next_tile(self):
        self._border.toggle_next_tile()
