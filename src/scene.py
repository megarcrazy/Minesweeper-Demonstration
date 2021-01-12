from src.object import Object


class Scene(Object):

    def __init__(self, screen):
        super().__init__(screen)
        self.next = self

    def switch_to_scene(self, scene):
        self.next = scene
