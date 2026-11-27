from core.component import Component
from components.spriterenderer import SpriteRenderer
from utility.vec2 import Vec2
from core.gamerenderer import GameRenderer
from core.gameobject import GameObject

class TilingManager(Component):
    def __init__(self, w, ground_tex, enabled=True):
        super().__init__(enabled)
        self.tiles = []
        self.step = w
        self.ground_tex = ground_tex
        self.spawned = False

    def start(self, params=None):
        self.camera = self.game_object.get_scene().camera
        self.ground = GameObject("Ground")
        self.ground.add_component(SpriteRenderer(self.ground_tex)).layer = -2000
        self.ground.get_component(SpriteRenderer).apply_camera_scaling = False

        camera = self.camera
        step = self.step
        width = GameRenderer.width * GameRenderer.canvas_scale * self.camera.render_scale
        height = GameRenderer.height * GameRenderer.canvas_scale * self.camera.render_scale
        render_center = camera.game_object.transform.position + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, GameRenderer.height / 2 * GameRenderer.canvas_scale)
        num_steps = int(-(-step // width))
        starting_pos = (render_center.x - (step * num_steps / 2)) - render_center.x

        self.ground.transform.position.x = 0
        self.ground.transform.position.y = 0
        self.ground.transform.scale.x = 10000
        self.ground.transform.scale.y = 10000


        

    def update(self, params=None):
        if (self.spawned):
            return

        to_add = []

        camera = self.camera
        step = self.step
        width = GameRenderer.width * GameRenderer.canvas_scale * self.camera.render_scale
        height = GameRenderer.height * GameRenderer.canvas_scale * self.camera.render_scale
        render_center = camera.game_object.transform.position + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, GameRenderer.height / 2 * GameRenderer.canvas_scale)
        num_steps = int(-(-step // width))
        starting_pos = (render_center.x - (step * num_steps / 2)) - render_center.x

        self.ground.transform.position.x = render_center.x
        self.ground.transform.position.y = (render_center.y + height * 0.5) - (render_center.y - self.game_object.transform.scale.y) * 0.5
        self.ground.transform.scale.x = GameRenderer.width * GameRenderer.canvas_scale * 2
        self.ground.transform.scale.y = GameRenderer.height * GameRenderer.canvas_scale* 0.5

        

        for i in range(3):
            t = GameObject("Tile")
            t.add_component(SpriteRenderer("bg1_tileable.png")).layer = -1000
            t.transform.scale = Vec2(step, self.game_object.transform.scale.y)
            t.transform.position = Vec2(starting_pos + step * i, self.game_object.transform.position.y + GameRenderer.height * 0.375)

        self.spawned = True







        



        

        