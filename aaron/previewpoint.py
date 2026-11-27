from core.component import Component
from core.time import Time
from utility.vec2 import Vec2

class PreviewPoint(Component):
    
    def __init__(self, target_scale, enabled=True):
        super().__init__(enabled)
        self.target_scale = target_scale

    def awake(self, params=None):
 
        self.game_object.transform.scale = Vec2(0, 0)
        self.__preview = False
        self.duration = 0.1
        self.elapsed_time = 0.0


    def set_preview(self, show):
        if (show == self.__preview):
            return

        self.elapsed_time = 0.0
        self.__preview = show

    def update(self, params=None):
        self.elapsed_time += Time.get_deltatime()
        t = self.elapsed_time / self.duration

        transform = self.game_object.transform

        if (self.__preview == True):
            if (t <= 1.0):
                transform.scale = Vec2.lerp(transform.scale, self.target_scale, t)
        else:
            if (t <= 1.0):
                transform.scale = Vec2.lerp(transform.scale, Vec2(0, 0), t)
        