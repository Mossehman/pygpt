from core.component import Component
from utility.mousemanager import MouseManager
from components.spriterenderer import SpriteRenderer
from core.eventhandler import AppEvent
from utility.vec2 import Vec2
import pygame

class Button(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)
        self.on_hover_enter = AppEvent()
        self.on_hover_exit = AppEvent()
        self.on_click = AppEvent()

        self.is_hovering = False
        self.can_click = True
        self.use_release = False

        self.sprite = None

    def start(self, params=None):
        self.sprite = self.game_object.get_component(SpriteRenderer)

    def update(self, params=None):
        mousePos = MouseManager.mouse_pos()
        rect = self.sprite.rect
        if (rect is None):
            return

        hoveringState = rect.collidepoint(mousePos.x, mousePos.y)

        if (hoveringState == True and self.is_hovering == False):
            self.is_hovering = True
            self.on_hover_enter.invoke()
        elif (hoveringState == False and self.is_hovering == True):
            self.is_hovering = False
            self.on_hover_exit.invoke()

        if (self.is_hovering == True and self.can_click):
            if ((self.use_release == True and MouseManager.mouse_up()) or (self.use_release == False and MouseManager.mouse_down())):
                self.on_click.invoke()
