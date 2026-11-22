from components.spriterenderer import SpriteRenderer

class AnimatedSpriteRenderer(SpriteRenderer):
    def __init__(self, image_path, enabled=True):
        super().__init__(image_path, enabled)
        self.animations = {} # Dictionary of all the animations
        self.interval = 0.2 # The interval between each frame of animation
        self.current_animation = "" # The string name of the currently-playing animation
        self.loop = False # Whether the animation will loop
        self.__current_frame = 0
    def add_animation(self, animation_name:str, animations:list):
        self.animations[animation_name] = animations


    def play_animation(self, animation_name, loop=False, interval=0.2):
        if (animation_name not in self.animations):
            return
        self.current_animation = animation_name
        self.__current_frame = 0
        self.loop = loop
        self.interval = interval

    def update(self, params=None):
        return