import pygame
from src.object import Object
import src.constant as c


class Command(Object):

    def __init__(self, screen):
        super().__init__(screen)
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)
