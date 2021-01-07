import pygame
from menu_src.menu import Menu
import constant as c


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Minesweeper Demonstration')
        self._screen = None
        self._state = True
        self.create_window()
        self._scene = Menu(self._screen)

    def run(self):
        while self._state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._state = False

            self.keyboard_input()
            self._scene.update()
            self._scene.render()
            self._scene = self._scene.next

            pygame.time.wait(1)
            pygame.display.flip()

    def create_window(self):
        self._screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    def keyboard_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.restart()

    def restart(self):
        self._scene = Menu(self._screen)
