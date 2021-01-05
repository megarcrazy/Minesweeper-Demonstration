import pygame
from menu_button import MenuButton
from scene_manager import SceneManager
import constant as c


class Menu(SceneManager):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self._buttons = []
        self.initialise()
        pygame.init()

    def initialise(self):
        pygame.font.init()
        self.initialise_play_button()

    def initialise_play_button(self):
        x = c.SCREEN_WIDTH // 2
        y = c.SCREEN_HEIGHT // 2
        width = 300
        height = 100
        rect = (x, y, width, height)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        play_button = MenuButton(self._screen, 'Play', font, rect)
        self._buttons.append(play_button)

    def update(self):
        self.update_buttons()

    def render(self):
        self._screen.fill(c.WHITE)
        self.display_buttons()
        pygame.display.flip()

    def update_buttons(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_left_click = pygame.mouse.get_pressed()[0]
        for button in self._buttons:
            scene = button.update(mouse_position, mouse_left_click)
            if scene:
                self.switch_to_scene(scene)

    def display_buttons(self):
        for button in self._buttons:
            button.display()