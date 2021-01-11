import pygame
from src.menu_scene.button_start import StartButton
from src.menu_scene.button_settings import SettingsButton
from src.menu_scene.button_instructions import InstructionsButton
from src.scene import Scene
from src import constant as c


class Menu(Scene):

    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self._buttons = []
        self.initialise()
        pygame.init()

    def initialise(self):
        self.initialise_buttons()

    def initialise_buttons(self):
        self._buttons.append(StartButton(self._screen))
        self._buttons.append(InstructionsButton(self._screen))
        self._buttons.append(SettingsButton(self._screen))

    def update(self):
        self.update_buttons()

    def render(self):
        self._screen.fill(c.WHITE)
        self.display_buttons()

    def update_buttons(self):
        for button in self._buttons:
            if button.update():
                next_scene = button.get_scene_pointer()
                self.switch_to_scene(next_scene)

    def display_buttons(self):
        for button in self._buttons:
            button.render()
