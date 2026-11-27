class Component:

    def __init__(self, enabled=True):
        self.__enabled = enabled
        self.game_object = None
        self.__ran_awake = False
        self.__ran_start = False

    def resolve(self):
        return self

    def awake(self):
        return

    def start(self, params=None):
        return
    
    def update(self, params=None):
        return

    def late_update(self, params=None):
        return

    def physics_update(self, params=None):
        return

    def before_render(self, params=None):
        return

    def after_render(self, params=None):
        return


    def set_enabled(self, enabled):
        self.__enabled = enabled

    def get_enabled(self):
        return self.__enabled


    def on_enabled(self):
        return

    def on_disabled(self):
        return

    
    def on_collision(self, params=None):
        return

    def on_collision_stay(self, params=None):
        return

    def on_collision_exit(self, params=None):
        return

    def on_trigger(self, params=None):
        return

    