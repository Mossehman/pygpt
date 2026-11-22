from core.time import Time
from utility.vec2 import Vec2
import math
from core.contact import CollisionContact

class PhysicsManager:
    PHYSICS_TICK = 0.05 # Interval between physics ticks
    GRAVITY = Vec2(0, 50)
    __elapsed_time = 0
    __ticks = 0

    __rigidbodies = []
    __colliders = []

    MAX_ITERATIONS = 32

    @staticmethod
    def register_collider(collider):
        PhysicsManager.__colliders.append(collider)

    @staticmethod
    def register_rb(rb):
        PhysicsManager.__rigidbodies.append(rb)

    @staticmethod
    def update_ticks():
        PhysicsManager.__elapsed_time += Time.get_deltatime()
        PhysicsManager.__ticks = 0
        while PhysicsManager.__elapsed_time >= PhysicsManager.PHYSICS_TICK:
            PhysicsManager.__ticks += 1
            PhysicsManager.__elapsed_time -= PhysicsManager.PHYSICS_TICK
        
    @staticmethod
    def get_ticks():
        return PhysicsManager.__ticks

    @staticmethod
    def run():
        cols = PhysicsManager.__colliders
        rbs = PhysicsManager.__rigidbodies
        for rb in rbs:
            for col in cols:
                if (rb.collider == None or rb.collider == col):
                    continue
                did_collide, simplex = PhysicsManager.check_collisions(rb.collider, col)
                if (did_collide):
                    if (rb.kinematic == True):
                        continue
                    normal, depth = PhysicsManager.resolve_collisions(rb.collider, col, simplex)

                    collision_data = (rb.collider, col, normal, depth)
                    rb.game_object.collision_event.invoke(collision_data)
                    col.game_object.collision_event.invoke(collision_data)

                    # rb.collider.game_object.transform.position = rb.game_object.transform.position - normal * depth


        return

    @staticmethod
    def cleanup():
        PhysicsManager.__colliders.clear()
        PhysicsManager.__rigidbodies.clear()

    @staticmethod
    def __support(a, b, dir):
        # get minkowsky difference between a and b along a dir
        return a.support(dir) - b.support(-dir)

    @staticmethod
    def __triple(p1, p2, p3):
        # perpendicular vector to a given edge
        return p2 * p1.dot(p3) - p1 * p2.dot(p3)

    @staticmethod
    # collision check algorithm that utilises the GJK algorithm
    # I fucking love this algorithm RAHHHHHHHHHHHHHHHHHHHHHHHHH
    # function js returns True or False if 2 objects collide, can be any shape and size
    def check_collisions(a, b):
        max_iterations = PhysicsManager.MAX_ITERATIONS # arbitrary iteration count for checking collisions

        simplex = [PhysicsManager.__support(a, b, Vec2(1, 0))] # list of corner points of the collision mesh we're constructing
        # ^ since this engine is in 2d, we only need to handle 2 edge cases: line (2pts) and triangle (3pts)
        
        dir = -simplex[0]

        for _ in range(max_iterations):
            if dir.dot(dir) < 0.00001:
                return True, simplex # lies in 0,0 range, we are colliding, yay!

            point = PhysicsManager.__support(a, b, dir)
            if (point.dot(dir) < 0):
                return False, simplex
            simplex.append(point)

            if (len(simplex) == 2):
                p1 = simplex[0] # point
                p2 = simplex[1] # newly added pt

                diff_vec = p1 - p2
                origin_vec = -p2

                dir = PhysicsManager.__triple(diff_vec, origin_vec, diff_vec) # Get next support point

            else:
                p1 = simplex[0] # oldest point
                p2 = simplex[1] # middle child LOLOLOLOLOLOLOLOL
                p3 = simplex[2] # newest point

                diff1 = p2 - p3
                diff2 = p1 - p3
                origin_vec = -p3

                diff1_perpendicular = PhysicsManager.__triple(diff2, diff1, diff1)
                diff2_perpendicular = PhysicsManager.__triple(diff1, diff2, diff2)

                if (diff1_perpendicular.dot(origin_vec) > 0):
                    simplex = [p2, p3]
                    dir = diff1_perpendicular
                elif (diff2_perpendicular.dot(origin_vec) > 0):
                    simplex = [p1, p3]
                    dir = diff2_perpendicular
                else:
                    return True, simplex

        return True, simplex

    @staticmethod
    def resolve_collisions(a, b, simplex):
        max_iterations = PhysicsManager.MAX_ITERATIONS
        poly = list(simplex) # copy the simplex for our polygon points so we don't fuck with the actual simplex collision mesh

        if (len(poly) == 2):
            p1 = poly[0]
            p2 = poly[1]

            e = p2 - p1

            for i in (Vec2(-e.y, e.x), Vec2(e.y, -e.x)):
                c = PhysicsManager.__support(a, b, i)
                if (abs(Vec2.cross(e, c - p1)) > 0.000001):
                    poly.append(c)
                    break

        if (len(poly) < 3):
            return Vec2(0, 0), 0.0 # The 2 polygons are LITERALLY just touching one another, don't needa resolve anything

        if (Vec2.cross(poly[1] - poly[0], poly[2] - poly[0]) < 0):
            temp = poly[1]
            poly[1] = poly[2]
            poly[2] = temp

        for _ in range(max_iterations):
            best_distance = math.inf # smallest distance of resolution to push the 2 colliders out of one another
            best_normal = None
            best_vert = 0

            for i in range(len(poly)):
                p1 = poly[i]
                p2 = poly[(i + 1) % len(poly)]
                e = p2 - p1

                if (e.dot(e) < 0.000001):
                    continue

                normal = Vec2(e.y, -e.x).normalize()
                distance = normal.dot(p1)

                if (distance < best_distance):
                    best_distance = distance
                    best_normal = normal
                    best_vert = i

            point = PhysicsManager.__support(a, b, best_normal)
            if (point.dot(best_normal) - best_distance < 0.00001):
                return best_normal, best_distance

            poly.insert(best_vert + 1, point)
        return best_normal, best_distance

            
