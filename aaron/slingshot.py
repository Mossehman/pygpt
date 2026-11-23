from core.component import Component
from components.rigidbody import Rigidbody
from utility.vec2 import Vec2
from utility.inputmanager import InputManager
import pygame


class SlingshotComponent(Component):
    def __init__(self, force_mult=1, enabled=True):
        super().__init__(enabled)
        self.force_mult = force_mult
        self.shoot_dir = Vec2(1, 0) # shoot straight by default
        self.charge = 0 # goes from 0 - 1

        self.temp_time = 1.0 # temp method for testing cos I lazy do mouse-to-world

    def update(self, params=None):
        if (InputManager.held_inputs(pygame.K_SPACE)):
            
