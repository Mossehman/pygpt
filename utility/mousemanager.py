import pygame
from core.gamerenderer import GameRenderer
from utility.vec2 import Vec2


class MouseManager:

    mouseDown = False 
    mouseHeld = False
    mouseReleased = False

    mouse_buttons = (False, False, False)

    # Converts a position in window pixels to a position on the canvas.
    @staticmethod
    def to_canvas(position):
        # Subtract the centring offset, then undo the scaling by dividing.
        return ((position[0] - GameRenderer.canvas_offset[0]) / GameRenderer.canvas_scale,
                (position[1] - GameRenderer.canvas_offset[1]) / GameRenderer.canvas_scale)

    # Returns where the mouse is, measured in canvas pixels.
    @staticmethod
    def mouse_pos():
        output = MouseManager.to_canvas(pygame.mouse.get_pos())
        return Vec2(output[0], output[1])

    @staticmethod
    def poll_events(event):
        MouseManager.mouse_buttons = pygame.mouse.get_pressed(num_buttons=3)
        if (event.type == pygame.MOUSEBUTTONDOWN):
            MouseManager.mouseHeld = True
            MouseManager.mouseDown = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            MouseManager.mouseHeld = False
            MouseManager.mouseReleased = True

    @staticmethod
    def initalise():
        MouseManager.mouseReleased = False
        MouseManager.mouseDown = False

    @staticmethod
    def flush_events():
        MouseManager.mouseHeld = False
        MouseManager.mouseDown = False
        MouseManager.mouseReleased = False

    @staticmethod
    def mouse_down():
        return MouseManager.mouseDown

    @staticmethod
    def mouse_held():
        return MouseManager.mouseHeld

    @staticmethod
    def mouse_up():
        return MouseManager.mouseReleased