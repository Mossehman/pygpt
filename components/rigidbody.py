from core.component import Component
from components.collider import Collider
from utility.vec2 import Vec2
from core.physicsmanager import PhysicsManager
import math

class Rigidbody(Component):
    def __init__(self, mass=60, enabled=True):
        super().__init__(enabled)
        self.kinematic = False
        self.freeze_rotation = False
        self.enable_gravity = True
        self.gravity_scale = 1.0
        self.__mass = mass
        self.velocity = Vec2(0, 0)
        self.angular_velocity = 0.0
        self.restitution = 0
        self.friction = 1.0
        self.collider = None
        self.__force = Vec2(0, 0)
        self.__torque = 0.0
        self.prev_pos = Vec2(0, 0)
        self.prev_rot = 0

    @staticmethod
    def cross_sv(w, r):
        return Vec2(-w * r.y, w * r.x)

    @property
    def inverse_mass(self):
        return 0.0 if self.kinematic else 1 / self.__mass

    @property
    def inverse_inertia(self):
        if self.kinematic or self.freeze_rotation or self.collider is None:
            return 0.0
        return 1 / self.collider.inertia(self.__mass)

    def awake(self):
        self.collider = self.game_object.get_component(Collider)
        if self.collider is None:
            print("Rigidbody could not find a collider!") # Every rigidbody NEEDS a collider
    
    def update(self, params=None):
        PhysicsManager.register_rb(self) # register rigidbody for force calculations

    def add_force(self, force, point=None):
        self.__force += force # we accumulate the force here and then output it all in 1 shot
        if point is not None:
            r = point - self.game_object.transform.position # vector from point of force impact to game object's center
            self.__torque += Vec2.cross(r, force) # calculate torque value based on the cross product

    def add_torque(self, torque):
        self.__torque += torque

    def add_impulse(self, impulse, point=None):
        # Impulse force applies directly to the velocity, rather than the usual acceleration math (Impulse -> instant acceleration via force)
        self.velocity += impulse * self.inverse_mass
        if point is not None:
            r = point - self.game_object.transform.position
            self.angular_velocity += Vec2.cross(r, impulse) * self.inverse_inertia

    def get_vel_from_impulse(self, impulse):
        return (impulse * (1 /  self.__mass))

    def get_pos_from_vel(self, vel):
        if (self.enable_gravity):
            vel += PhysicsManager.GRAVITY * PhysicsManager.PHYSICS_TICK * self.gravity_scale
        
        return vel * PhysicsManager.PHYSICS_TICK, vel

    def velocity_at(self, point):
        r = point - self.game_object.transform.position 
        return self.velocity + Rigidbody.cross_sv(self.angular_velocity, r)

    def physics_update(self, params=None):
        self.prev_pos = Vec2(self.game_object.transform.position.x, self.game_object.transform.position.y)
        self.prev_rot = self.game_object.transform.rotation
        # shorthand some of our variables so code is more readable
        dt = PhysicsManager.PHYSICS_TICK
        transform = self.game_object.transform

        if self.kinematic:
            self.velocity, self.angular_velocity = Vec2(0, 0), 0.0 # object is kinematic, cannot be affected by physics
        else:
            if self.enable_gravity:
                self.velocity += PhysicsManager.GRAVITY * dt * self.gravity_scale # apply gravity via velocity (so we don't accelerate as we fall)
            self.velocity += self.__force * (self.inverse_mass * dt) # velocity math (a=f/m, v=a/t)
            self.angular_velocity += self.__torque * self.inverse_inertia * dt # angular velocity based on inertia, this rotates everything

        # reset all the accumulative data or we'll infinitely accelerate/spin
        # holy shit it spins, is that a jojo reference?!??!
        # ahahahahahaha kill me
        self.__force = Vec2(0, 0)
        self.__torque = 0.0 

        transform.position += self.velocity * dt # position finally updates and we get our movement
        transform.rotation -= math.degrees(self.angular_velocity * dt) # Pygame is weird with angles for some reason, so negative rotation is clockwise instead of calculated counterclockwise


    def late_update(self, params=None):
        self.game_object.transform.render_position = self.prev_pos + (self.game_object.transform.position - self.prev_pos) * PhysicsManager.alpha
        self.game_object.transform.render_rotation = self.prev_rot + (self.game_object.transform.rotation - self.prev_rot) * PhysicsManager.alpha