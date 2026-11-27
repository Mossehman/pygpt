import utility.scenecontext as scenecontext
from utility.mousemanager import MouseManager


class SceneManager:
    __active_scenes = {}
    scenecontext.current_scene = None

    # For better control of our code lifecycle, we only load and unload the scenes we want at fixed points in code, rather than immediately
    # Therefore, we cache which scenes we want to load and unload for later
    __to_load = [] # list of scenes to load 
    __to_unload = [] # list of scene names to unload 
    # Loads a new game scene
    # If additive is True, loads the scene on top of the existing scenes on the next frame
    # If additive is False, unloads all current scenes and loads the new scene on the next frame
    # Pass a scene object into the scene parameter

    @staticmethod
    def load_scene(scene, additive=False):
        if scene.get_name() in SceneManager.__active_scenes:
            SceneManager.__to_unload.append(scene.get_name())
        if (additive == False):
            for k, v in SceneManager.__active_scenes.items():
                SceneManager.__to_unload.append(k)
        
        SceneManager.__to_load.append(scene)
        return True
    

    # Since we're working with additive scenes, we also need to be able to unload them when needed

    @staticmethod
    def unload_scene(scene_name: str):
        if (len(SceneManager.__active_scenes) <= 1):
            print("Too little scenes to unload, one scene should always be active!")
            return
        if scene_name in SceneManager.__active_scenes:
            SceneManager.__to_unload.append(scene_name)

    @staticmethod
    def get_current():
        return scenecontext.current_scene

    @staticmethod
    def run_scenes():

        # Unload all scenes that need to be unloaded first
        for unload in SceneManager.__to_unload:
            SceneManager.__active_scenes[unload].on_unload()
            del SceneManager.__active_scenes[unload]

        # Handle scenes that need to be loaded up
        for load in SceneManager.__to_load:
            SceneManager.__active_scenes[load.get_name()] = load
            scenecontext.current_scene = load
            MouseManager.flush_events()
            load.scene_default_load()
            load.on_load()

        SceneManager.__to_load = []
        SceneManager.__to_unload = []
        
        for k, scene in SceneManager.__active_scenes.items():
            scenecontext.current_scene = scene # Keep track of which scene is the current one being updated
            scene.run_scene() # Update each scene in the list of scenes

    @staticmethod
    def get_scenes():
        return f"Active: {SceneManager.__active_scenes}, Loading: {SceneManager.__to_load}"