import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
import src.constant as c


class Settings(Scene):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self._back_message = BackMessage(self._screen)

    def render(self):
        self._screen.fill(c.WHITE)
        self._back_message.render()
