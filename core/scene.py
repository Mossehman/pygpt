from core.gamerenderer import GameRenderer
from test.print_component import PrintComponent
from core.eventhandler import AppEvent
from core.physicsmanager import PhysicsManager

class Scene:

    def __init__(self, name):
        self.__name = name

        self.initialise_event = AppEvent()
        self.start_event = AppEvent() # Runs when the component is initialised
        self.update_event = AppEvent() # Runs once per frame
        self.late_update_event = AppEvent() # Runs after the update event
        self.physics_event = AppEvent() # Runs every physics tick, physics tick runs at a fixed interval rather than per-frame, can run once, multiple times, or none per frame

        self.render_start_event = AppEvent() # Runs before the game scene is rendered
        self.render_end_event = AppEvent() # Runs after the game scene is rendered
        self.app_cleanup_event = AppEvent() # Runs at the end of every game tick (cleans up all gameObjects flagged for deletion)

    def get_name(self):
        return self.__name

    def on_load(self):
        raise NotImplementedError("Add game objects to derived scene classes, not base scene")

    def run_scene(self):
        self.initialise_event.invoke()
        self.start_event.invoke()
        self.update_event.invoke()
        self.late_update_event.invoke()

        for _ in range(PhysicsManager.get_ticks()):
            self.physics_event.invoke()
            PhysicsManager.run()

        PhysicsManager.cleanup()

        # Rendering goes AFTER all the game logic
        self.render_start_event.invoke()
        GameRenderer.render()
        self.render_end_event.invoke()

        # Cleanup all objects flagged to be destroyed
        self.app_cleanup_event.invoke()

    def on_unload(self):
        return


    
