import sys
import pygame
import utility.gamerunning as gamerunning
from final.gamescene import GameScene
from final.gamescene2 import GameScene2
from final.gamescene3 import GameScene3
from core.scenemanager import SceneManager
from core.time import Time
from core.gamerenderer import GameRenderer
from core.physicsmanager import PhysicsManager
from utility.inputmanager import InputManager
from utility.mousemanager import MouseManager
from test.test_scene import TestScene
from final.startscene import StartScene


class Application:

    def start(self):
        my_scene = GameScene2("Test scene")
        SceneManager.load_scene(my_scene)
        pass
    
    def run(self):
        GameRenderer.init_screen()
        while gamerunning.is_game_running:
            Time.run() # Update the stopwatch accordingly
            PhysicsManager.update_ticks()
            GameRenderer.update_layout()
            InputManager.initialise()
            MouseManager.initalise()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamerunning.is_game_running = False
                    break
                GameRenderer.translate_event(event)
                MouseManager.poll_events(event)
                InputManager.poll_events(event)
            SceneManager.run_scenes()
            pygame.display.flip()

        pygame.quit()