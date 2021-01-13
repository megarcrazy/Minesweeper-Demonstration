import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
from src.settings_window.setting import Setting
import src.constant as c


class Settings(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self._back_message = BackMessage(self._screen)
        self._texts = []
        self.initialise_texts()

    def render(self):
        self._screen.fill(c.WHITE)
        self._back_message.render()
        self.render_commands()

    def render_commands(self):
        for text in self._texts:
            text.render()

    def initialise_texts(self):
        x, y = 10, 10
        self._texts.append(Setting(self._screen, x, y, c.BLACK,
                                   "Sweep button: Left mouse button"))
        self._texts.append(Setting(self._screen, x, y + c.FONT_SIZE, c.BLACK,
                                   "Restart Button: r"))
        self._texts.append(Setting(self._screen, x, y + c.FONT_SIZE * 2, c.BOMB_TILE_COLOUR,
                                   "This is the colour of revealed bomb tiles."))
        self._texts.append(Setting(self._screen, x, y + c.FONT_SIZE * 3, c.UNREVEALED_TILE_COLOUR,
                                   "This is the colour of unrevealed tiles."))
        self._texts.append(Setting(self._screen, x, y + c.FONT_SIZE * 4, c.QUEUED_TILE_COLOUR,
                                   "This is the colour of queued tile borders tiles."))
        self._texts.append(Setting(self._screen, x, y + c.FONT_SIZE * 5, c.NEXT_TILE_COLOUR,
                                   "This is the colour of the dequeued tile border."))
