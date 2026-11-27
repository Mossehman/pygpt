from utility.vec2 import Vec2
from core.component import Component
from core.time import Time

class HoverEffect(Component):
    def __init__(self, size_mult, time, enabled=True):
        super().__init__(enabled)
        self.size_mult = size_mult
        self.time = time
        self.elapsed_time = 0.0
        self.is_hovering = False

    def start(self, params=None):
        self.original_scale = self.game_object.transform.scale + Vec2()

    def on_hover_enter(self, params=None):
        self.is_hovering = True
        self.elapsed_time = 0.0

    def on_hover_exit(self, params=None):
        self.is_hovering = False
        self.elapsed_time = 0.0

    def update(self, params=None):
        self.elapsed_time += Time.get_deltatime_unscaled()
        t = self.elapsed_time / self.time

        if (t > 1.0):
            t = 1.0

        if (self.is_hovering):
            self.game_object.transform.scale = Vec2.lerp(self.game_object.transform.scale, self.original_scale * self.size_mult, t)
        else: 
            self.game_object.transform.scale = Vec2.lerp(self.game_object.transform.scale, self.original_scale, t)