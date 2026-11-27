import math
import pygame


class Vec2:
    # UP = Vec2(0, 1)
    # RIGHT = Vec2(1, 0)

    def __init__(self, x=0.0, y=0.0):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other:float):
        return Vec2(self.x / other, self.y / other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.yet

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def sqr_magnitude(self):
        return self.x ** 2 + self.y ** 2
    
    def normalize(self):
        return self.divide(self.magnitude())
    
    def to_degree(self):
        return (math.atan2(self.y, self.x) * (180 / math.pi) + 360) % 360

    def scale(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    def to_angle(self):
        return math.atan2(self.y, self.x)

    def to_py(self):
        return pygame.Vector2((self.x, self.y))

    def to_tuple(self):
        return (self.x, self.y)

    def divide(self, other):
        x = 0
        if (math.fabs(self.x) > 0):
            x = self.x / other
            
        y = 0
        if (math.fabs(self.y) > 0):
            y = self.y / other
        return Vec2(x, y)

    def reflect(self, normal):
        return self - normal * 2 * (self.dot(normal) / (normal.dot(normal)))
    
    @staticmethod
    def lerp(a, b, t):
        return (a * (1 - t)) + (b * t)

    @staticmethod
    def cross(a, b):
        return a.x * b.y - a.y * b.x
        
        