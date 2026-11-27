from core.component import Component
from core.time import Time
from utility.vec2 import Vec2


class GameCamera(Component):

    def __init__(self, enabled=True):
        super().__init__(enabled)

        self.attached_bird = None
        self.move_speed = 20

        self.__elapsed_time = 0
        self.move_back_time = 2
        self.has_bird = False
        self.camera_scale = 0.6
        self.is_aiming = False
        self.aim_time = 0.3
        return

    def start(self, params=None):
        self.starting_pos = self.game_object.transform.position - Vec2()

    def set_attached_bird(self, bird):
        self.attached_bird = bird
        self.has_bird = True

    def bird_die(self, params=None):
        self.attached_bird = None
        self.__elapsed_time = 0.0

    def set_aiming(self, params):
        self.is_aiming = params
        self.__elapsed_time = 0.0

    def late_update(self, params=None):
        if (self.attached_bird is not None):
            targetPos = Vec2(self.attached_bird.game_object.transform.position.x, self.starting_pos.y)
            
            self.game_object.transform.position.x = Vec2.lerp(self.game_object.transform.position, targetPos, Time.get_deltatime() * self.move_speed).x
            # print(self.game_object.transform.position)
            self.game_object.transform.position.x = max(self.starting_pos.x, min(1200 * self.game_object.get_scene().camera.render_scale, self.game_object.transform.position.x))
        elif self.is_aiming:
            self.__elapsed_time += Time.get_deltatime()
            t = min(1.0, self.__elapsed_time / self.aim_time)
            lerp = lambda a,b,v : (a * (1 - v)) + (b * v)
            self.game_object.get_scene().camera.render_scale = lerp(self.game_object.get_scene().camera.render_scale, self.camera_scale, t)
            self.game_object.transform.position.y = lerp(self.game_object.transform.position.y, self.starting_pos.y - 320, t)

        else:
            self.__elapsed_time += Time.get_deltatime()
            t = min(1.0, self.__elapsed_time / self.move_back_time)

            self.game_object.transform.position = Vec2.lerp(self.game_object.transform.position, self.starting_pos, t)

        if self.is_aiming == False:
            self.__elapsed_time += Time.get_deltatime()
            t = min(1.0, self.__elapsed_time / self.aim_time)
            lerp = lambda a,b,v : (a * (1 - v)) + (b * v)
            self.game_object.get_scene().camera.render_scale = lerp(self.game_object.get_scene().camera.render_scale, 1.0, t)
            self.game_object.transform.position.y = lerp(self.game_object.transform.position.y, self.starting_pos.y, t)