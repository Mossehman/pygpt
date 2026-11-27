from utility.vec2 import Vec2
from core.component import Component
from core.gamerenderer import GameRenderer

class ScreenRatio(Component):
    def __init__(self, enabled=True):
        super().__init__(enabled)

    def start(self, params=None):
        self.xRatio = self.game_object.transform.position.x / GameRenderer.width
        self.yRatio = self.game_object.transform.position.y / GameRenderer.height 

    def late_update(self, params=None):
        self.game_object.transform.position.x = GameRenderer.width / GameRenderer.canvas_scale * self.xRatio
        self.game_object.transform.position.y = GameRenderer.height / GameRenderer.canvas_scale * self.yRatio
