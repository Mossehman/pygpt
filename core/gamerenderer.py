import pygame
from utility.vec2 import Vec2 

class GameRenderer:
    render_queue = []
    gizmo_queue = []

    width = 1200
    height = 800
    base_window_size = (0, 0)
    fullscreen = False
    can_resize = True

    window = None
    canvas = None
    canvas_scale = 1.0
    canvas_offset = (0, 0)
    background_src = None
    background = None
    background_size = (0, 0)

    @staticmethod
    def init_screen():
        info = pygame.display.Info()
        desktop_height = info.current_h if info.current_h > 0 else GameRenderer.height
        start_height = max(300, min(GameRenderer.height, int(desktop_height * 0.85)))
        start_width = int(start_height * GameRenderer.width / GameRenderer.height)

        GameRenderer.base_window_size = (start_width, start_height)

        if (GameRenderer.can_resize == True):
            GameRenderer.window = pygame.display.set_mode(GameRenderer.base_window_size, pygame.RESIZABLE)
        else:
            GameRenderer.window = pygame.display.set_mode(GameRenderer.base_window_size, pygame.NOFRAME)

        GameRenderer.canvas = pygame.Surface((GameRenderer.width, GameRenderer.height))
        GameRenderer.update_layout()

    @staticmethod
    def toggle_fullscreen():
        if (GameRenderer.fullscreen):
            resize_mode = pygame.RESIZABLE
            if (GameRenderer.can_resize == False):
                resize_mode = pygame.NOFRAME
            
            GameRenderer.window = pygame.display.set_mode(GameRenderer.base_window_size, resize_mode)
        else:
            GameRenderer.base_window_size = GameRenderer.window.get_size()
            GameRenderer.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        GameRenderer.fullscreen = not GameRenderer.fullscreen

    @staticmethod
    def enqueue_for_rendering(image_path:str, rect, priority:int):
        GameRenderer.render_queue.append((image_path, rect, priority))

    @staticmethod
    def enqueue_gizmo(draw_func):
        GameRenderer.gizmo_queue.append(draw_func)

    @staticmethod
    def set_backdrop(image):
        GameRenderer.background_src = image

    @staticmethod
    def update_layout():
        # Always ask pygame for the current window surface; its size changes when the user resizes.
        GameRenderer.window = pygame.display.get_surface()
        window_width, window_height = GameRenderer.window.get_size()
        # The largest scale that still fits both ways; min() keeps the whole canvas visible.
        GameRenderer.scale = min(window_width / GameRenderer.width, window_height / GameRenderer.height)
        # Size of the canvas once scaled.
        scaled_width = int(GameRenderer.width * GameRenderer.scale)
        scaled_height = int(GameRenderer.height * GameRenderer.scale)
        # Centre the scaled canvas; the leftover space is split evenly on both sides.
        GameRenderer.offset = ((window_width - scaled_width) // 2, (window_height - scaled_height) // 2)

    # Rewrites mouse events so their coordinates are canvas pixels. Without this,
    # clicking would hit the wrong spot whenever the window is not 640x800.
    @staticmethod
    def translate_event(event):
        # Only mouse events carry a position; everything else passes through unchanged.
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            # Copy the event's data into a normal dictionary we can edit.
            data = dict(event.dict)
            # Replace the window position with the canvas position.
            data["pos"] = GameRenderer.to_canvas(event.pos)
            # Motion events also have a "rel" (how far the mouse moved), which needs scaling too.
            if event.type == pygame.MOUSEMOTION:
                data["rel"] = (event.rel[0] / GameRenderer.scale, event.rel[1] / GameRenderer.scale)
            # Build a fresh event of the same type carrying the corrected data.
            return pygame.event.Event(event.type, data)
        return event

    @staticmethod
    def render():
        window_width, window_height = GameRenderer.window.get_size()
        # Rebuild the stretched backdrop only when the window size has changed.
        if GameRenderer.background_src is not None and GameRenderer.background_size != (window_width, window_height):
            GameRenderer.background = pygame.transform.smoothscale(GameRenderer.background_src, (window_width, window_height))
            # Multiply by grey to darken it, so the bars look like a dim frame around the game.
            GameRenderer.background.fill((110, 110, 110), special_flags=pygame.BLEND_MULT)
            GameRenderer.background_size = (window_width, window_height)
        # Fill the whole window first (this is what shows in the bars next to the canvas).
        if GameRenderer.background is not None:
            GameRenderer.window.blit(GameRenderer.background, (0, 0))
        else:
            GameRenderer.window.fill((0, 0, 0))
        # Stretch the canvas to its scaled size; smoothscale blends pixels so it looks clean.
        scaled = pygame.transform.smoothscale(
            GameRenderer.canvas, (int(GameRenderer.width * GameRenderer.scale), int(GameRenderer.height * GameRenderer.scale)))
        # Place it at the centring offset.
        GameRenderer.window.blit(scaled, GameRenderer.offset)
        GameRenderer.canvas.fill((0, 0, 0))

        GameRenderer.render_queue = sorted(GameRenderer.render_queue, key=lambda w: w[2]) # sort by priority of rendering
        for draw_call in GameRenderer.render_queue:
            sprite = draw_call[0]
            rect = draw_call[1]
            GameRenderer.canvas.blit(sprite, rect)

        for draw_fn in GameRenderer.gizmo_queue:
            draw_fn(GameRenderer.canvas)
        GameRenderer.gizmo_queue.clear()

        GameRenderer.render_queue.clear()
            
        scaled = pygame.transform.smoothscale(
        GameRenderer.canvas,
        (int(GameRenderer.width * GameRenderer.scale), int(GameRenderer.height * GameRenderer.scale)))
        GameRenderer.window.blit(scaled, GameRenderer.offset)


