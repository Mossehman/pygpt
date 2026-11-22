from core.eventhandler import AppEvent
from core.component import Component
from components.transform import Transform
import utility.scenecontext as scenecontext

class GameObject:
    def __init__(self, name=""):
        self.name = name
        self.__current_scene = scenecontext.current_scene
        self.collision_event = AppEvent()

        if (self.__current_scene == None):
            return # Should not be possible for there to be no current scene
        self.components = set()
        self.components_queue = set() # These components have not yet been inialised, we should ignore them for now
        self.__current_scene.initialise_event.add_listener(self.init_components)
        self.transform = self.add_component(Transform())

    
    # Adds a component to the gameobject
    def add_component(self, c: Component):
        c.game_object = self
        c.awake()
        if (c.get_enabled() == False):
            self.components_queue.add(c)
        else:
            self.components.add(c)
            self.__current_scene.start_event.add_listener_oneshot(c.start())
            self.hook_events(c)
        return c


    # Returns a component by type, put in the specific component class to output, returns None if nothing is found
    def get_component(self, t: type):
        for component in self.components:
            if isinstance(component, t):
                return component

    
    def init_components(self, params=None):
        initialised_components = []
        for component in self.components_queue:
            if (component.get_enabled() == False):
                continue
            self.__current_scene.start_event.add_listener_oneshot(component.start()) # Start() should only run once regardless if enabled or disabled multiple times, manually call it

            initialised_components.append(component)

        for component in initialised_components:
            self.components.add(component)
            self.hook_events(component) # Hook/rehook the component to it's respective events
            self.components_queue.discard(component) # Component has been initalised, we should get rid of it now


    def hook_events(self, c: Component):
        # Components will hook onto the scene's events, so they can all be processed together
        self.__current_scene.update_event.add_listener(c.update)
        self.__current_scene.late_update_event.add_listener(c.late_update)
        self.__current_scene.physics_event.add_listener(c.physics_update)
        self.__current_scene.render_start_event.add_listener(c.before_render)
        self.__current_scene.render_end_event.add_listener(c.after_render)
        self.collision_event.add_listener(c.on_collision_enter)

    def unhook_events(self, c: Component):
        # Unhook from the scene's events, this is either when the component is disabled/destroyed or the gameobject is inactive/destroyed
        self.__current_scene.update_event.remove_listener(c.update)
        self.__current_scene.late_update_event.remove_listener(c.late_update)
        self.__current_scene.physics_event.remove_listener(c.physics_update)
        self.__current_scene.render_start_event.remove_listener(c.before_render)
        self.__current_scene.render_end_event.remove_listener(c.after_render)
        self.collision_event.remove_listener(c.on_collision_enter)