from core.component import Component
from core.physicsmanager import PhysicsManager
from utility.vec2 import Vec2

class Collider(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)
        self.show_collider = False # Debug gizmo for rendering the collider shape\
        self.draw_color = (0, 255, 0)
        self.center = Vec2(0, 0)
        self.rb = None

    def support(self):
        raise NotImplementedError("No collision shape found")

    def render_collider(self):
        raise NotImplementedError("No collision shape found")

    def update(self, params=None):
        if (self.get_enabled()):
            PhysicsManager.register_collider(self)

    def after_render(self, params=None):
        if (self.show_collider == False):
            return
        self.render_collider()

    def inertia(self, mass):
        raise NotImplementedError("No collision shape found")

    def feature(self, d):
        return [self.support(d)]