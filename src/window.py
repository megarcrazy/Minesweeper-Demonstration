import pygame
from src.menu_window.menu_scene import Menu
import constant as c


class Window:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Minesweeper Demonstration')
        self._state = True
        self._screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self._scene = Menu(self._screen)

    def run(self):
        while self._state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._state = False

            # Check for keyboard input in the pygame window
            self.keyboard_input()

            self._scene.update()
            self._scene.render()

            # Scene changes if the scene next pointer is not pointing to itself
            self.manage_scene()

            pygame.time.wait(1)

            # Draw pixels on the pygame window
            pygame.display.flip()

    def keyboard_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.restart()

    def restart(self):
        self._scene = Menu(self._screen)

    def manage_scene(self):
        self._scene = self._scene.next
