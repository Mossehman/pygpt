from core.component import Component
from components.spriterenderer import SpriteRenderer
from core.gameobject import GameObject
from components.circlecollider import CircleCollider
from components.rigidbody import Rigidbody
from rainier.bombkb import BombKB

class Bomb(Component):
    def __init__(self, explosion_size):
        self.explosion_size = explosion_size
        super().__init__(True)

    def start(self, params=None):
       pass
    
    def on_collision(self, params=None):
        print("yes")
        boomeffect = GameObject("Fire")
        boomeffect.add_component(SpriteRenderer("boom.png"))
        boomeffect.transform.position = self.game_object.transform.position
        boomeffect.transform.scale.x = 100
        boomeffect.transform.scale.y = 100
        boomeffect.add_component(BombKB(10000000))
        boomeffect.add_component(CircleCollider(self.explosion_size)).trigger = True

        self.game_object.destroy()


        

