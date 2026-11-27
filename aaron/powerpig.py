from aaron.pig import Pig
from core.gameobject import GameObject
from aaron.barrier import Barrier
from components.circlecollider import CircleCollider
from components.collider import Collider
from components.spriterenderer import SpriteRenderer

class PowerPig(Pig):
    def __init__(self, radius, enabled=True):
        super().__init__(enabled)
        self.barrier = None
        self.radius = radius
    def prayer(self):
        barrier = GameObject("Barrier")
        # barrier.add_component(SpriteRenderer("boom.png"))
        barrier.add_component(Barrier(self.radius))
        barrier.transform.position = self.game_object.transform.position
        barrier.transform.scale.x = self.radius
        barrier.transform.scale.y = self.radius
        # barrier.add_component(SpriteRenderer("gravitywell.png")).layer = -1
        barrier.add_component(CircleCollider(0.5))
        barrier.get_component(Collider).trigger = True
        barrier.get_component(Collider).collider_layer = "barrier"
        self.barrier = barrier
    def start(self, params=None):
        super().start(params)
        self.prayer()

    def update(self, params=None):
        self.barrier.transform.position = self.game_object.transform.position