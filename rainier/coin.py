from core.component import Component
from components.spriterenderer import SpriteRenderer
from core.gameobject import GameObject
from components.polygoncollider import PolygonCollider
from components.rigidbody import Rigidbody
from components.circlecollider import CircleCollider
from utility.vec2 import Vec2
class Coin(Component):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(True)
    def start(self, params=None):
        coin = GameObject("Coin")
        coin.add_component(SpriteRenderer("coinv2.png"))
        coin.add_component(CircleCollider(0.5)).show_collider = True
        coin.transform.position = self.game_object.transform.position
        coin.transform.scale.x = 50
        coin.transform.scale.y = 50
        coin.add_component(Rigidbody()).restitution = 0.7
        coin.get_component(Rigidbody).gravity_scale = 4
    