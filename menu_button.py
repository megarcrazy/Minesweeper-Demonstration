import pygame
from button import Button
from play import Play
import constant as c


class MenuButton(Button):

    def __init__(self, screen, text, font, rect):
        super().__init__(screen, text, font, rect)
        self._colour = c.TOMATO
        self._is_clicked = False

    def update(self, mouse_position, mouse_left_click):
        return self.check_on_click(mouse_position, mouse_left_click)

    def display(self):
        pygame.draw.rect(self._screen, self._colour, self._rect)
        self.display_text()

    def display_text(self):
        text = self._font.render(self._text, False, (0, 0, 0))
        x = self._centre[0]
        y = self._centre[1]
        text_rect = text.get_rect(center=(x, y))
        self._screen.blit(text, text_rect)

    def check_on_click(self, mouse_position, mouse_left_click):
        is_hover = self.check_hover(mouse_position)
        clicked = mouse_left_click
        if is_hover:
            self._colour = c.LIGHT_SALMON
            if self._is_clicked and not clicked:
                return Play(self._screen)
            self._is_clicked = mouse_left_click
        else:
            self._colour = c.TOMATO

    def check_hover(self, mouse_position):
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        within_x = self._rect[0] < mouse_x < self._rect[0] + self._rect[2]
        within_y = self._rect[1] < mouse_y < self._rect[1] + self._rect[3]
        if within_x and within_y:
            return True
        return False
