from components.collider import Collider
from components.transform import Transform
from utility.vec2 import Vec2
import pygame
from core.gamerenderer import GameRenderer
import math

class CircleCollider(Collider):
    def __init__(self, radius:float, enabled=True):
        super().__init__(enabled)
        self.__width = radius
        self.__height = radius
        self.center = Vec2(0, 0)

    def support(self, d):
        t = self.game_object.transform
        a = math.radians(t.rotation)
        c, s = math.cos(a), math.sin(a)
        
        lx = d.x * c - d.y * s
        ly = d.x * s + d.y * c

        ex = lx * t.scale.x * self.__width
        ey = ly * t.scale.y * self.__height

        n = math.hypot(ex, ey) or 1
        local = Vec2(self.__width * ex / n, self.__height * ey / n)

        return t.transform_point(local)

    def render_collider(self):
        t = self.game_object.transform
        pts = []
        for i in range(32):
            a = 2 * math.pi * i / 32
            local = Vec2(math.cos(a) * self.__width, math.sin(a) * self.__height)
            pts.append(t.transform_point(local).to_tuple())
        GameRenderer.enqueue_gizmo(
            lambda surface: pygame.draw.polygon(surface, self.draw_color, pts, width=2))


    def inertia(self, mass):
        s = self.game_object.transform.scale
        w = self.__width * s.x
        h = self.__height * s.y
        return mass * (w * w + h * h) / 4