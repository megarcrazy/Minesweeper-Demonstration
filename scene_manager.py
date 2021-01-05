class SceneManager:

    def __init__(self):
        self.next = self

    def update(self):
        pass

    def render(self):
        pass

    def switch_to_scene(self, scene):
        self.next = scene
