class Object:

    def __init__(self, screen):
        self._screen = screen

    def update(self):
        pass

    def render(self):
        pass

    def print_self_type(self):
        print(type(self).__name__)