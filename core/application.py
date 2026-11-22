import sys
import pygame
from test.test_scene import TestScene
from core.scenemanager import SceneManager
from core.time import Time
from core.gamerenderer import GameRenderer
from core.physicsmanager import PhysicsManager
from utility.inputmanager import InputManager

class Application:

    def start(self):
        scene_manager = SceneManager()
        my_scene = TestScene("Test scene")
        scene_manager.load_scene(my_scene)
        pass
    
    def run(self):
        self.running = True
        scene_manager = SceneManager()
        GameRenderer.init_screen()
        while self.running:
            Time.run() # Update the stopwatch accordingly
            PhysicsManager.update_ticks()
            GameRenderer.update_layout()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                InputManager.poll_events(event)
            scene_manager.run_scenes()
            pygame.display.flip()

        pygame.quit()