import pygame
from src.gameobject import GameObject
import src.constant as c


class BackMessage(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        # This gives the user a quick reminder on how to return to the main menu.
        self._text = "Press 'r' to go back to the menu"

        # This message is located at the bottom of the screen in the instructions
        # and the settings scene.
        self._x, self._y = c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT - 20
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)

    def render(self):
        text = self._font.render(self._text, False, (0, 0, 0))
        text_rect = text.get_rect(center=(self._x, self._y))
        self._screen.blit(text, text_rect)
