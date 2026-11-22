from core.scene import Scene
from utility.singleton import Singleton
import utility.scenecontext as scenecontext


class SceneManager(metaclass=Singleton):
    def __init__(self):
        self.__active_scenes = {}
        scenecontext.current_scene = None

        # For better control of our code lifecycle, we only load and unload the scenes we want at fixed points in code, rather than immediately
        # Therefore, we cache which scenes we want to load and unload for later
        self.__to_load = [] # list of scenes to load 
        self.__to_unload = [] # list of scene names to unload 

    # Loads a new game scene
    # If additive is True, loads the scene on top of the existing scenes on the next frame
    # If additive is False, unloads all current scenes and loads the new scene on the next frame
    # Pass a scene object into the scene parameter
    def load_scene(self, scene, additive=False):
        if scene.get_name() in self.__active_scenes:
            self.__to_unload.append(scene.get_name())
        if (additive == False):
            for k, v in self.__active_scenes.items():
                self.__to_unload.append(k)
        
        self.__to_load.append(scene)
        return True
    

    # Since we're working with additive scenes, we also need to be able to unload them when needed
    def unload_scene(self, scene_name: str):
        if (len(self.__active_scenes) <= 1):
            print("Too little scenes to unload, one scene should always be active!")
            return
        if scene_name in self.__active_scenes:
            self.__to_unload.append(scene_name)

    def get_current(self):
        return scenecontext.current_scene

    def run_scenes(self):

        # Unload all scenes that need to be unloaded first
        for unload in self.__to_unload:
            self.__active_scenes[unload].on_unload()
            del self.__active_scenes[unload]

        # Handle scenes that need to be loaded up
        for load in self.__to_load:
            self.__active_scenes[load.get_name()] = load
            scenecontext.current_scene = load
            load.on_load()

        self.__to_load = []
        self.__to_unload = []
        
        for k, scene in self.__active_scenes.items():
            scenecontext.current_scene = scene # Keep track of which scene is the current one being updated
            scene.run_scene() # Update each scene in the list of scenes

    def get_scenes(self):
        return f"Active: {self.__active_scenes}, Loading: {self.__to_load}"