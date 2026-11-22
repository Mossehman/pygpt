import math

from core.component import Component
from utility.vec2 import Vec2

class Transform(Component):

    def __init__(self, enabled=True):
        super().__init__(enabled)
        self.position = Vec2(0, 0)
        self.local_scale = Vec2(1, 1)
        self.scale = Vec2(1, 1)
        self.rotation = 0 # Rotation angle between 0-360
        self.hierarchy = [] # List of child transforms

    def transform_point(self, p):
        x = p.x * self.scale.x
        y = p.y * self.scale.y

        angle = math.radians(self.rotation)
        cosine = math.cos(angle)
        sine = math.sin(angle)

        old_x = x
        x = old_x * cosine + y * sine
        y = -old_x * sine + y * cosine

        return Vec2(x + self.position.x, y + self.position.y)
    