from core.component import Component
from components.transform import Transform
from utility.vec2 import Vec2
from core.time import Time
from utility.inputmanager import InputManager
import pygame

class TestMovement(Component):
    def __init__(self, speed, enabled=True):
        super().__init__(enabled)
        self.speed = speed # Movement speed

    def start(self, params=None):
        return

    def update(self, params=None):
        attached_gameobject = self.game_object # -> This gets us the game object that contains this component
        gameobjects_transform = attached_gameobject.transform # -> The game object has a transform component

        # gameobjects_transform.rotation -= 40 * Time.get_deltatime()

        position = gameobjects_transform.position # -> The position of the game object now

        input_dir = Vec2(0, 0)
        if InputManager.key_held(pygame.K_w):
            input_dir.y -= 1
        if InputManager.key_held(pygame.K_s):
            input_dir.y += 1

        if InputManager.key_held(pygame.K_a):
            input_dir.x -= 1

        if InputManager.key_held(pygame.K_d):
            input_dir.x += 1

        input_dir = input_dir.normalize()
        gameobjects_transform.position = position + input_dir * self.speed * Time.get_deltatime()
        # Multiplying the speed by delta time ensures the character moves consistently regardless of frame rate
        return
