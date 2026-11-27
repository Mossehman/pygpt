from core.component import Component
from utility.vec2 import Vec2
from components.rigidbody import Rigidbody
from components.collider import Collider
from components.spriterenderer import SpriteRenderer
from core.gameobject import GameObject
from aaron.barriervfx import BarrierVFX

class Barrier(Component):
    def __init__(self, radius):
        super().__init__(True)
        self.radius = radius
        self.barrier_effects = []

        delay = 0
        layer = -1
        for i in range(5):
            barrier_vfx = GameObject("Barrier VFX")
            barrier_vfx.add_component(BarrierVFX(delay, Vec2(radius, radius)))
            barrier_vfx.add_component(SpriteRenderer("gravitywell.png")).layer = layer
            self.barrier_effects.append(barrier_vfx)
            delay += 4 / 5
            layer -= 1
        

    def update(self, params=None):
        for vfx in self.barrier_effects:
            vfx.transform.position = self.game_object.transform.position

    def on_trigger(self, params=None):
        # barrier = GameObject("Barrier")
        # barrier.add_component(SpriteRenderer("boom.png"))
        # barrier.transform.position = self.game_object.transform.position
        # barrier.transform.scale.x = 300
        # barrier.transform.scale.y = 300
        # barrier.add_component(CircleCollider(0.5)).show_collider = True
        # barrier.get_component(Collider).trigger = True

        collider_to_test = params
        rb = collider_to_test.game_object.get_component(Rigidbody)
        if (rb is None):
            return
        rb.add_force((rb.game_object.transform.position - self.game_object.transform.position).normalize() * 500000)
