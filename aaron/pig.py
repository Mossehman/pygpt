from utility.vec2 import Vec2
from core.component import Component
from components.collider import Collider
from components.rigidbody import Rigidbody
from utility.inputmanager import InputManager
import pygame

from test.test_scene import TestScene
from core.scenemanager import SceneManager

class Pig(Component):

    def __init__(self, enabled=True):
        self.velocity_threshold = 180
        self.collider = None
        super().__init__(enabled)

    def start(self, params=None):
        self.collider = self.game_object.get_component(Collider)

    def on_collision(self, params):

        if (self.collider is None):
            return
        
        colliderToCheck = None
        if (params[0] == self.collider):
            colliderToCheck = params[1]
        elif(params[1] == self.collider):
            colliderToCheck = params[0]

        if colliderToCheck is None:
            return
        
        rb = colliderToCheck.game_object.get_component(Rigidbody)
        if (rb is None):
            return
        
        collision_magnitude = rb.velocity.sqr_magnitude()
        if (collision_magnitude > self.velocity_threshold ** 2):
            self.game_object.destroy()