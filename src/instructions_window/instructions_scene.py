import pygame
from src.scene import Scene
from src.helper_objects.back_message import BackMessage
from src.instructions_window.text_body import TextBody
import src.constant as c


class Instructions(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self._back_message = BackMessage(self._screen)
        self._text_body = TextBody(self._screen)
        pygame.init()

    def render(self):
        self._screen.fill(c.WHITE)
        self._back_message.render()
        self._text_body.render()
