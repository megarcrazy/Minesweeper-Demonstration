import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
from src.settings_scene.command_sweep import SweepCommand
from src.settings_scene.command_restart_program import RestartProgramCommand
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
        self._texts.append(SweepCommand(self._screen))
        self._texts.append(RestartProgramCommand(self._screen))
