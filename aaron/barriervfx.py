from core.component import Component
from utility.vec2 import Vec2
from components.rigidbody import Rigidbody
from components.collider import Collider
from components.spriterenderer import SpriteRenderer
from core.gameobject import GameObject
from core.time import Time

class BarrierVFX(Component):
    def __init__(self, delay, scale):
        super().__init__(True)
        self.elapsed_time = 0.0
        self.delay = delay
        self.can_play = False
        self.to_destroy = False
        self.effect_duration = 4
        self.starting_scale = scale + Vec2()
        
    def awake(self, params=None):
        self.game_object.transform.scale = Vec2()

    def update(self, params=None):
        if (self.can_play == False):
            self.elapsed_time += Time.get_deltatime()
            if (self.elapsed_time >= self.delay):
                self.can_play = True
                self.elapsed_time = 0
                self.game_object.transform.scale = Vec2()
        else:
            self.elapsed_time += Time.get_deltatime()
            t = self.elapsed_time / self.effect_duration
            self.game_object.transform.scale = Vec2.lerp(self.game_object.transform.scale, self.starting_scale, t)
            if (t >= 0.5):
                self.game_object.transform.scale = Vec2()
                self.elapsed_time = 0.0