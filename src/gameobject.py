class GameObject:

    def __init__(self, screen):
        self._screen = screen

    # Updates class variables
    def update(self):
        pass

    # Render is the interaction between objects and pygame graphics.
    # All object render functions do not change class variables.
    def render(self):
        pass

    def print_self_type(self):
        print(type(self).__name__)
