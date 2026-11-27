from core.component import Component
from components.rigidbody import Rigidbody
from utility.vec2 import Vec2
from utility.inputmanager import InputManager
import pygame
from core.time import Time
from core.gameobject import GameObject
from components.spriterenderer import SpriteRenderer
from components.circlecollider import CircleCollider
from utility.mousemanager import MouseManager
from core.physicsmanager import PhysicsManager
from aaron.previewpoint import PreviewPoint
from core.eventhandler import AppEvent



class SlingshotComponent(Component):
    def __init__(self, birds, force_mult=1, enabled=True):
        super().__init__(enabled)
        self.force_mult = force_mult
        self.shoot_dir = Vec2(1, 0) # shoot straight by default
        self.charge = 0 # goes from 0 - 1

        self.max_mouse_magnitude = 500
        self.init_mouse_pos = Vec2(0, 0)
        self.attached_body = None
        self.attached_bird = None
        self.distance = 100
        
        self.elapsed_time = 0.0
        self.delay_points = 0.05

        self.num_points = 10
        self.point_iterations = 4
        self.current_drawn_index = 0
        self.points_list = []

        self.cam_elapsed = 0.0
        self.cam_duration = 0.4
        self.target_range = 0.6
        self.current_range = 1.0

        for i in range(self.num_points):
            point = GameObject("Point")
            point.add_component(SpriteRenderer("circle.png"))
            p = point.add_component(PreviewPoint(Vec2(20, 20)))
            self.points_list.append(p)

        self.draw_points = True


        self.birds = birds
        self.current_bird_index = 0
        self.no_birds_event = AppEvent()
        self.bird_shoot_event = AppEvent()
        self.bird_die_event = AppEvent()
        self.aim_event = AppEvent()
        self.can_shoot = True
        self.charged = False
        self.bird_spacing = 70

        self.cancelled = False


    def start(self, params=None):
        if (self.current_bird_index >= len(self.birds)):
            self.no_birds_event.invoke()
            return

        self.attached_bird = self.birds[self.current_bird_index]
        self.attached_body = self.birds[self.current_bird_index].game_object.get_component(Rigidbody)
        self.attached_bird.game_object.transform.position = self.game_object.transform.position + Vec2()
        print(self.game_object.transform.position)
        self.can_shoot = True

    def update(self, params=None):
        current_spacing = 0
        for i in range(self.current_bird_index + 1, len(self.birds)):
            current_spacing -= self.bird_spacing
            self.birds[i].game_object.transform.position.x = self.game_object.transform.position.x + current_spacing # set x position to match the spacing
        
        if (self.cancelled and MouseManager.mouse_up() and MouseManager.mouse_buttons[2] == False and MouseManager.mouse_buttons[0] == False):
            self.cancelled = False


        if (self.can_shoot == False or self.attached_bird is None or self.attached_body is None or self.cancelled == True):
            return

        
        if (MouseManager.mouse_held() and MouseManager.mouse_buttons[2]):
            
            self.aim_event.invoke(False)
            self.charge = 0.0
            self.cancelled = True
            self.charged = False
            self.elapsed_time = 0.0
            self.current_drawn_index = 0
            for p in self.points_list:
                p.set_preview(False)
            return

        if (MouseManager.mouse_down() and MouseManager.mouse_buttons[0]):
            self.init_mouse_pos = MouseManager.mouse_pos()

        if (MouseManager.mouse_held() and MouseManager.mouse_buttons[0]):
            startingPoint = self.game_object.transform.position
            starting_vel = self.attached_body.get_vel_from_impulse(self.shoot_dir * self.charge * self.force_mult)
            for p in self.points_list:
                for i in range(self.point_iterations):
                    v = self.attached_body.get_pos_from_vel(starting_vel)
                    startingPoint += v[0]
                    starting_vel = v[1]
                p.game_object.transform.position = startingPoint

            magnitude = min(self.max_mouse_magnitude, (MouseManager.mouse_pos() - self.init_mouse_pos).magnitude())
            if (magnitude > 0):
                self.charged = True
                self.charge = magnitude / self.max_mouse_magnitude
                self.shoot_dir = (self.init_mouse_pos - MouseManager.mouse_pos()).normalize()
                self.attached_body.kinematic = True
                self.attached_body.game_object.transform.position = self.game_object.transform.position - self.shoot_dir * (self.distance * self.charge)
                self.current_range = self.target_range
                self.aim_event.invoke(True)

            self.elapsed_time += Time.get_deltatime()
            if (self.elapsed_time >= self.delay_points and self.current_drawn_index < len(self.points_list)):
                self.elapsed_time = 0.0
                self.points_list[self.current_drawn_index].set_preview(True)
                self.current_drawn_index += 1
        
        elif (MouseManager.mouse_up() and self.charged and MouseManager.mouse_buttons[0] == False and self.cancelled == False):
            self.aim_event.invoke(False)
            self.current_range = 1.0
            self.attached_bird.launched = True
            self.attached_body.kinematic = False
            self.attached_body.add_impulse(self.shoot_dir * self.charge * self.force_mult)
            self.charge = 0.0
            self.elapsed_time = 0.0
            self.current_drawn_index = 0
            self.can_shoot = False
            self.charged = False
            self.bird_shoot_event.invoke(self.attached_bird)
            self.attached_bird.death_event.add_listener_oneshot(self.on_bird_die)
            for p in self.points_list:
                p.set_preview(False)

    def on_bird_die(self, params=None):
        self.bird_die_event.invoke()
        self.current_bird_index += 1

        if (self.current_bird_index >= len(self.birds)):
            self.no_birds_event.invoke()
            return

        self.attached_bird = self.birds[self.current_bird_index]
        self.attached_body = self.birds[self.current_bird_index].game_object.get_component(Rigidbody)
        self.attached_bird.game_object.transform.position = self.game_object.transform.position + Vec2()
        self.can_shoot = True


            

    # def late_update(self, params=None):
    #     PhysicsManager.raycast_shape.show_collider = True
    #     raycast = PhysicsManager.raycast(self.game_object.transform.position, Vec2(1000, 0), 25000)
    #     if (raycast is not None):
    #         print(raycast[0].game_object.name)
    #         self.attached_body.game_object.transform.position = raycast[1]
    #     pass
    