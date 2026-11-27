from core.time import Time
from utility.vec2 import Vec2
import math
from core.contact import CollisionContact

class PhysicsManager:
    PHYSICS_TICK = 0.02 * Time.time_scale # Interval between physics ticks
    MAX_PHYSICS_TICK = 5 # Interval between physics ticks
    GRAVITY = Vec2(0, 250)
    MAX_ITERATIONS = 8
    OVERLAP = 0.5
    CORRECTION = 0.4

    raycast_shape = None

    collision_layers = {}


    __elapsed_time = 0
    __ticks = 0

    __rigidbodies = {}
    __colliders = []
    alpha = 0

    @staticmethod
    def add_ignore_collision(layerA, layerB):
        if (layerA in PhysicsManager.collision_layers):
            PhysicsManager.collision_layers[layerA].append(layerB)
        else:
            PhysicsManager.collision_layers[layerA] = [layerB]

        if (layerB in PhysicsManager.collision_layers):
            PhysicsManager.collision_layers[layerB].append(layerA)
        else:
            PhysicsManager.collision_layers[layerB] = [layerA]

    
    @staticmethod
    def remove_ignore_collision(layerA, layerB):
        if (layerA in PhysicsManager.collision_layers):
            PhysicsManager.collision_layers[layerA].remove(layerB)
            if (len(PhysicsManager.collision_layers[layerA]) == 0):
                del PhysicsManager.collision_layers[layerA]
        
        if (layerB in PhysicsManager.collision_layers):
            PhysicsManager.collision_layers[layerB].remove(layerA)
            if (len(PhysicsManager.collision_layers[layerB]) == 0):
                del PhysicsManager.collision_layers[layerB]

    @staticmethod
    def register_collider(collider):
        PhysicsManager.__colliders.append(collider)

    @staticmethod
    def register_rb(rb):
        if (rb.collider == None):
            return
        PhysicsManager.__rigidbodies[rb.collider.resolve()] = rb

    @staticmethod
    def update_ticks():
        PhysicsManager.alpha = PhysicsManager.__elapsed_time / PhysicsManager.PHYSICS_TICK
        PhysicsManager.__elapsed_time += Time.get_deltatime()
        PhysicsManager.__ticks = 0
        while PhysicsManager.__elapsed_time >= PhysicsManager.PHYSICS_TICK:
            PhysicsManager.__ticks = min(PhysicsManager.__ticks + 1, PhysicsManager.MAX_PHYSICS_TICK)
            PhysicsManager.__elapsed_time -= PhysicsManager.PHYSICS_TICK
        
    @staticmethod
    def get_ticks():
        return PhysicsManager.__ticks

    @staticmethod
    def raycast(start, direction, distance, layers:list=None):
        normalized_dir = direction.normalize()
        p1 = start
        p2 = start + normalized_dir * distance

        PhysicsManager.raycast_shape.p1 = p1
        PhysicsManager.raycast_shape.p2 = p2

        PhysicsManager.raycast_shape.draw_p1 = p1
        PhysicsManager.raycast_shape.draw_p2 = p2

        nearest_distance = math.inf

        for col in PhysicsManager.__colliders:
            if (col.trigger == True):
                continue
            
            hit, simplex = PhysicsManager.check_collisions(PhysicsManager.raycast_shape, col)
            if (hit == False):
                continue

            normal, depth = PhysicsManager.resolve_collisions(PhysicsManager.raycast_shape, col, simplex)
            if (depth <= 0):
                continue

            depth_vector = normalized_dir * depth
            point = p2 - depth_vector
            
            PhysicsManager.raycast_shape.draw_p2 = point
            PhysicsManager.raycast_shape.render_collider()
            return (col, point, normal, depth)

        PhysicsManager.raycast_shape.render_collider()
        return None
    


    @staticmethod
    def run():
        cols = PhysicsManager.__colliders
        rbs = PhysicsManager.__rigidbodies
        col_contacts = []

        for i, col in enumerate(cols):
            for other in cols[i + 1:]: # do not check colliders we already accounted for
                rb_a, rb_b = rbs.get(col), rbs.get(other)

                if (col.collider_layer in PhysicsManager.collision_layers and other.collider_layer in PhysicsManager.collision_layers[col.collider_layer]):
                    continue

                if CollisionContact.get_inverse_mass(rb_a) == 0 and CollisionContact.get_inverse_mass(rb_b) == 0:
                    continue
                hit, simplex = PhysicsManager.check_collisions(col, other)
                if (hit == False):
                    continue

                if (col.trigger == True or other.trigger == True):
                    col.game_object.trigger_event.invoke(other)
                    other.game_object.trigger_event.invoke(col)
                    continue

                normal, depth = PhysicsManager.resolve_collisions(col, other, simplex)
                if (depth <= 0):
                    continue

                for point, point_depth in PhysicsManager.contact_points(col, other, normal, depth):
                    col_contacts.append(CollisionContact(rb_a, rb_b, point, normal, point_depth))

                collision_data = (col, other, normal, depth)
                col.game_object.collision_event.invoke(collision_data)
                other.game_object.collision_event.invoke(collision_data)
        
        for c in col_contacts:
            c.pre_step(PhysicsManager.PHYSICS_TICK, PhysicsManager.GRAVITY)

        for _ in range(PhysicsManager.MAX_ITERATIONS):
            for c in col_contacts:
                c.solve()

        for c in col_contacts:
            c.correct_position(PhysicsManager.OVERLAP, PhysicsManager.CORRECTION)

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


    @staticmethod
    def __clip(p1, p2, tangent, lowest, highest):
        d1 = tangent.dot(p1)
        d2 = tangent.dot(p2)
        out = [p for p, d in ((p1, d1), (p2, d2)) if lowest <= d <= highest]
        for bound in (lowest, highest):
            if (d1 - bound) * (d2 - bound) < 0:
                out.append(p1 + (p2 - p1) * ((bound - d1) / (d2 - d1)))
        return out


    @staticmethod
    def contact_points(a, b, n, depth):
        fa, fb = a.feature(n), b.feature(-n)
        if len(fa) == 1 and len(fb) == 1:
            return [((fa[0] + fb[0]) * 0.5, depth)]
        if len(fa) == 1:
            return [(fa[0], depth)]
        if len(fb) == 1:
            return [(fb[0], depth)]

        # Two edges: the one most perpendicular to n is the reference face,
        # the other edge is clipped against it.
        flat = lambda f: abs((f[1] - f[0]).normalize().dot(n))
        t = Vec2(-n.y, n.x)
        if flat(fa) <= flat(fb):
            ref, inc = fa, fb
            plane = n.dot(a.support(n))
            pen = lambda p: plane - n.dot(p)
        else:
            ref, inc = fb, fa
            plane = (-n).dot(b.support(-n))
            pen = lambda p: plane + n.dot(p)
        lo, hi = sorted((t.dot(ref[0]), t.dot(ref[1])))
        pts = [(p, pen(p)) for p in PhysicsManager.__clip(inc[0], inc[1], t, lo, hi)]
        pts = [(p, d) for p, d in pts if d >= -1e-6]
        return pts or [((a.support(n) + b.support(-n)) * 0.5, depth)]
