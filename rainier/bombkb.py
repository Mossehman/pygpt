from core.component import Component
from utility.vec2 import Vec2
from components.rigidbody import Rigidbody
from components.collider import Collider

class BombKB(Component):
    def __init__(self, kb, enabled=True):
        super().__init__(enabled)
        self.collided = False
        self.can_collide = True
        self.kb = kb

    def awake(self):
        self.collider = self.game_object.get_component(Collider)

    def physics_update(self, params):
        self.collided = True

    def on_trigger(self, params):
        if (self.can_collide == False):
            return

        other = params

        otherRB = other.game_object.get_component(Rigidbody)
        if (otherRB is None):
            return

        dirVal = (other.game_object.transform.position - self.game_object.transform.position).normalize()
        magnitude = (self.game_object.transform.position - other.game_object.transform.position).magnitude()
        otherRB.add_impulse(dirVal * (self.kb / magnitude))

    def late_update(self, params):
        if (self.collided):
            self.can_collide = False
