import math
from utility.vec2 import Vec2

class CollisionContact:
    def __init__(self, rigidbodyA, rigidbodyB, point, normal, depth):
        self.rigidbodyA = rigidbodyA
        self.rigidbodyB = rigidbodyB
        self.point = point
        self.normal = normal
        self.depth = depth

        self.normal_total = 0.0
        self.tangent_total = 0.0
    
    def __get_inverse_mass(self, rb):
        if (rb != None):
            return rb.inverse_mass
        return None

    def __get_inverse_inertia(self, rb):
        if (rb != None):
            return rb.inverse_inertia
        return None

    def __velocity_at(self, rb, point):
        return rb.velocity_at(point) if rb else Vec2(0, 0)

    def __effective_mass(self, direction):
        relativeA_dir = Vec2.cross(self.relativeA, direction)
        relativeB_dir = Vec2.cross(self.relativeB, direction)

        relative_speed = (self.__get_inverse_mass(self.rigidbodyA) + self.__get_inverse_mass(self.rigidbodyB) 
                          + relativeA_dir ** 2 * self.__get_inverse_inertia(self.rigidbodyA)
                          + relativeB_dir ** 2 * self.__get_inverse_inertia(self.rigidbodyB))
    
        if (relative_speed <= 0):
            return 0.0

        return 1 / relative_speed # this is how much force we would need to apply against the body to push it

    def __relative_velocity(self):
        return self.__velocity_at(self.b, self.point) - self.__velocity_at(self.a, self.point)

    def __push(self, impulse):
        if (self.rigidbodyA != None):
            self.rigidbodyA.add_impulse(-impulse, self.point)
        if (self.rigidbodyB != None):
            self.rigidbodyB.add_impulse(impulse, self.point)


    def pre_step(self, timestep, gravity):
        a = self.rigidbodyA
        b = self.rigidbodyB
        normal = self.normal 

        self.relativeA = self.point - self.rigidbodyA.game_object.transform.position if self.rigidbodyA else Vec2(0, 0)
        self.relativeB = self.point - self.rigidbodyB.game_object.transform.position if self.rigidbodyB else Vec2(0, 0)
        self.tangent = Vec2(-normal.y, normal.x)
        self.mass_normal = self.__effective_mass(normal)
        self.mass_tangent = self.__effective_mass(self.tangent)

        bodies = [r for r in (a, b) if r]
        frictions = [r.friction for r in bodies]
        self.mu = math.sqrt(frictions[0] * frictions[1]) if len(frictions) == 2 else frictions[0]
        e = min(r.restitution for r in bodies)

        vn = self.__relative_velocity().dot(normal)
        rest_speed = 2 * math.hypot(gravity.x, gravity.y) * timestep
        self.target_vn = -e * vn if vn < -rest_speed else 0.0

    def solve(self):
        normal = self.normal
        tangent = self.tangent

        vn = self.__relative_velocity().dot(normal) # velocity along normal vector
        delta = self.mass_normal * (self.target_vn - vn)
        original_normal = self.normal_total
        self.normal_total = max(original_normal + delta, 0.0)
        self.__push(normal * (self.normal_total - original_normal))

        vt = self.__relative_velocity().dot(tangent) # velocity along tangent vector
        delta = self.mass_tangent * -vt
        limit = self.mu * self.normal_total
