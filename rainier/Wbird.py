import math
from utility.vec2 import Vec2
from components.rigidbody import Rigidbody
from core.component import Component
from components.spriterenderer import SpriteRenderer
from core.gameobject import GameObject
from components.polygoncollider import PolygonCollider
from components.circlecollider import CircleCollider
from components.collider import Collider
from rainier.coin import Coin
from rainier.bomb import Bomb
from core.time import Time
from utility.mousemanager import MouseManager
from rainier.RBird import Bird

class Whitebird(Bird):
    def __init__(self, x, y):
        super().__init__(x, y)
    def Boyage(self):
        boom = GameObject("Bomb")
        boom.add_component(Bomb(2))
        boom.add_component(SpriteRenderer("child bomb.png"))
        boom.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "bomb"
        boom.transform.position = self.game_object.transform.position + Vec2(0, 100)
        boom.transform.scale.x = 50
        boom.transform.scale.y = 50
        boom.add_component(Rigidbody()).restitution = 0.0


    def ability(self):
        self.Boyage()