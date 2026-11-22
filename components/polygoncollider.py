from components.collider import Collider
from components.transform import Transform
from utility.vec2 import Vec2
import pygame
from core.gamerenderer import GameRenderer

class PolygonCollider(Collider):

    __box_points = [Vec2(0.5, 0.5), Vec2(0.5, -0.5), Vec2(-0.5, -0.5), Vec2(-0.5, 0.5)]
    __tri_points = [Vec2(0.5, 1/3), Vec2(-0.5, 1/3), Vec2(0, -2/3)]

    def __init__(self, points:list, enabled=True):
        super().__init__(enabled)
        self.__points = points
        for p in self.__points:
            self.center += p

        self.center /= len(self.__points)

    def support(self, d):
        world_points = []
        for p in self.__points:
            world_points.append(self.game_object.transform.transform_point(p))
        return max(world_points, key=lambda p: p.dot(d))

    def render_collider(self):
        pts = [self.game_object.transform.transform_point(p).to_tuple() for p in self.__points]
        GameRenderer.enqueue_gizmo(
            lambda surface: pygame.draw.polygon(surface, self.draw_color, pts, width=2))

    def inertia(self, mass):
        scale = self.game_object.transform.scale
        pts = [Vec2(p.x * scale.x, p.y * scale.y) for p in self.__points]
        num = den = 0.0
        for i in range(len(pts)):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            c = abs(a.x * b.y - a.y * b.x)
            num += c * (a.dot(a) + a.dot(b) + b.dot(b))
            den += c
        return mass * num / (6 * den)


    @staticmethod
    def TRIANGLE():
        return PolygonCollider.__tri_points

    @staticmethod
    def BOX():
        return PolygonCollider.__box_points

    def feature(self, d):
        t = self.game_object.transform
        pts = [t.transform_point(p) for p in self.__points]

        # The corner farthest in direction d
        i = max(range(len(pts)), key=lambda k: pts[k].dot(d))
        prev, v, nxt = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]

        # Of the two edges meeting at that corner, return the one that faces d most directly
        # (its direction is closest to perpendicular to d)
        dn = d.normalize()
        if abs((v - prev).normalize().dot(dn)) <= abs((nxt - v).normalize().dot(dn)):
            return [prev, v]
        return [v, nxt]

    


    