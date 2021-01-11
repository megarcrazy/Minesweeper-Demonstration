import pygame
from src.object import Object
import src.constant as c


class Button(Object):

    def __init__(self, screen):
        self._x = None
        self._y = None
        self._width, self._height = 300, 100
        self._rect = None
        self._colour = None
        self._font = None
        self._centre = None
        self._text = None
        self.screen = screen
        self._screen = self.screen
        self._is_clicked = False
        self._font = pygame.font.SysFont(c.FONT, c.BUTTON_FONT_SIZE)
        self._scene_pointer = None

    def check_on_click(self):
        mouse_left_click = pygame.mouse.get_pressed(3)[0]
        clicked = mouse_left_click
        if self.check_hover():
            if self._is_clicked and not clicked:
                return True
            self._is_clicked = mouse_left_click
        return False

    def check_hover(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_position
        within_x = self._rect[0] < mouse_x < self._rect[0] + self._rect[2]
        within_y = self._rect[1] < mouse_y < self._rect[1] + self._rect[3]
        if within_x and within_y:
            return True
        return False

    def render(self):
        pygame.draw.rect(self._screen, self._colour, self._rect)
        self.display_text()

    def display_text(self):
        text = self._font.render(self._text, False, (0, 0, 0))
        x, y = self._centre
        text_rect = text.get_rect(center=(x, y))
        self._screen.blit(text, text_rect)

    def set_rectangle(self):
        rect = (self._x, self._y, self._width, self._height)
        return rect

    def get_scene_pointer(self):
        return self._scene_pointer

    @staticmethod
    def centre_rectangle(rect):
        centre_x, centre_y, width, height = rect
        x = centre_x - width // 2
        y = centre_y - height // 2
        new_rect = (x, y, width, height)
        return new_rect
