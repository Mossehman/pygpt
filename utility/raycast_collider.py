from components.collider import Collider
from components.transform import Transform
from utility.vec2 import Vec2
import pygame
from core.gamerenderer import GameRenderer
from core.physicsmanager import PhysicsManager

class RaycastCollider(Collider):

    def __init__(self, enabled=True):
        super().__init__(enabled)
        self.p1 = Vec2(0, 0)
        self.p2 = Vec2(0, 0)
        self.draw_p1 = Vec2(0, 0)
        self.draw_p2 = Vec2(0, 0)
        PhysicsManager.raycast_shape = self

    def support(self, d):
        return max(self.p1, self.p2, key=lambda p: p.dot(d))

    def render_collider(self):
        if (self.show_collider == True):
            GameRenderer.enqueue_gizmo(
                lambda surface: pygame.draw.line(surface, self.draw_color, self.draw_p1.to_tuple(), self.draw_p2.to_tuple(), width=2))

    def inertia(self, mass):
        return 0

    def feature(self, d):
        return None

    def update(self, params):
        return

    


    