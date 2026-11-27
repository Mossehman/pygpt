from core.component import Component
from utility.vec2 import Vec2
from core.time import Time

class Camera(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)
        self.render_scale = 0.9
        self.__priority = 0 

    def set_priority(self, priority):
        self.__priority = priority
        if (self.__priority >= self.game_object.get_scene().camera.priority):
            self.game_object.get_scene().camera = self

    # def update(self, params=None):
    #     self.game_object.transform.position.x -= 100 * Time.get_deltatime()
