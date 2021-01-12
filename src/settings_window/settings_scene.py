import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
from src.settings_window.command_sweep import SweepCommand
from src.settings_window.command_restart import RestartCommand
from src.settings_window.setting_bomb_colour import SettingsBombColour
from src.settings_window.setting_tile_colour import SettingsTileColour
from src.settings_window.setting_tile_border_colour import SettingsTileBorderColour
from src.settings_window.setting_next_tile_border_colour import SettingsNextTileBorderColour
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
        self._texts.append(SweepCommand(self._screen, x, y))
        self._texts.append(RestartCommand(self._screen, x, y + c.FONT_SIZE))
        self._texts.append(SettingsBombColour(self._screen, x, y + c.FONT_SIZE * 2))
        self._texts.append(SettingsTileColour(self._screen, x, y + c.FONT_SIZE * 3))
        self._texts.append(SettingsTileBorderColour(self._screen, x, y + c.FONT_SIZE * 4))
        self._texts.append(SettingsNextTileBorderColour(self._screen, x, y + c.FONT_SIZE * 5))
