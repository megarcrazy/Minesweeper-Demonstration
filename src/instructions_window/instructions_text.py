import pygame
from src.object import Object
import src.constant as c


class TextBody(Object):

    def __init__(self, screen):
        super().__init__(screen)
        self._text = self.break_text(
            "Start by clicking any tile and the algorithm "
            + "will sweep the tiles if possible. Selecting "
            + "a tile with no adjacent bombs will cause unchecked "
            + "surrounding tiles to be appended to a queue. "
            + "All unchecked tiles in the queue are labelled by "
            + "a border surrounding the tile in the grid. "
            + "Then the circular tracker shows the current "
            + "sweep location."
        )
        self._x, self._y = 10, 10
        self._font = pygame.font.SysFont(c.FONT, c.FONT_SIZE)

    def render(self):
        vertical_text_gap = 0
        for line in self._text:
            text = self._font.render(line, False, (0, 0, 0))
            self._screen.blit(text, (self._x, self._y + vertical_text_gap))
            vertical_text_gap += c.FONT_SIZE

    # Input text and the function splits the string into lines up to
    # the length "split_size" and returns an array of strings.
    @staticmethod
    def break_text(text):
        broken_text = []
        split_size = 45
        text = text.split(" ")
        character_count = start_of_split = 0

        i = 0
        while i < len(text) - 1:
            character_count += len(text[i]) + 1
            if character_count + len(text[i + 1]) > split_size:
                line = " ".join(text[start_of_split:i + 1])
                broken_text.append(line)
                character_count -= split_size
                start_of_split = i + 1
            i += 1

        line = " ".join(text[start_of_split:])
        broken_text.append(line)

        return broken_text
