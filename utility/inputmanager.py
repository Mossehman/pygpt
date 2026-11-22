import pygame

# Static class for getting user input
class InputManager:
    pressed_inputs = set()
    held_inputs = set()
    released_inputs = set()

    @staticmethod
    def poll_events(event):
        InputManager.pressed_inputs = set()
        InputManager.released_inputs = set()

        if (event.type == pygame.KEYDOWN):
            InputManager.pressed_inputs.add(event.key)
            InputManager.held_inputs.add(event.key)
        elif (event.type == pygame.KEYUP):
            InputManager.released_inputs.add(event.key)
            InputManager.held_inputs.discard(event.key)

        return
    
    @staticmethod
    def key_pressed(key):
        return key in InputManager.pressed_inputs

    @staticmethod
    def key_held(key):
        return key in InputManager.held_inputs

    @staticmethod
    def key_released(key):
        return key in InputManager.released_inputs