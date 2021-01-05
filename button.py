import pygame
from rectangle import Rectangle
import constant as c


class Button:

    def __init__(self, screen, text, font, rect):
        self._screen = screen
        self._text = text
        self._font = font
        self._centre = rect[:2]
        self._rect = Rectangle.centre_rectangle(rect)
