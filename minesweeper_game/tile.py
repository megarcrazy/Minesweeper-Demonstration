import pygame
import constant as c


class Tile:

    def __init__(self, screen, x, y, size, font):
        self._screen = screen
        self._x = x
        self._y = y
        self._size = size
        self._font = font

        self._colour = c.DARK_TURQUOISE
        self._revealed = False
        self._bomb = False
        self._adjacent_bombs_count = 0

        self._hover = False
        self._is_clicked = False
        self._border = False
        self._border_colour = c.BLACK

    def update(self):
        if not self._revealed:
            if self._hover:
                self._colour = c.POWDER_BLUE
            else:
                self._colour = c.DARK_TURQUOISE
        else:
            if self._bomb:
                self._colour = c.RED
            else:
                self._colour = c.WHITE_SMOKE
        self._border = False
        self._border_colour = c.BLACK
        self._hover = False

    def render(self):
        self.render_tile_picture()
        self.render_tile_text()

    def render_tile_picture(self):
        x = self._x * self._size
        y = self._y * self._size
        rect = (x, y, self._size - 1, self._size - 1)
        pygame.draw.rect(self._screen, self._colour, rect)
        if self._border:
            border_thickness = 5
            x = self._x * self._size + border_thickness // 2
            y = self._y * self._size + border_thickness // 2
            size = self._size - border_thickness
            rect = (x, y, size, size)
            pygame.draw.rect(self._screen, self._border_colour, rect, border_thickness)

    def render_tile_text(self):
        if self._revealed and not self._bomb and self._adjacent_bombs_count != 0:
            text = self._font.render(str(self._adjacent_bombs_count), False, (0, 0, 0))
            x = int(self._size * (self._x + 0.5))
            y = int(self._size * (self._y + 0.5))
            text_rect = text.get_rect(center=(x, y))
            self._screen.blit(text, text_rect)

    def set_hover_is_true(self):
        self._hover = True

    def set_clicked(self, clicked):
        self._is_clicked = clicked

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

    def change_colour(self, colour):
        self._border_colour = colour

    def toggle_on_border(self):
        self._border = True
