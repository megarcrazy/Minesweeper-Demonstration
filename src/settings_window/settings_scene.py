import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
from src.settings_window.command_sweep import SweepCommand
from src.settings_window.command_restart import RestartCommand
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
