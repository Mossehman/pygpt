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

class Purple(Bird):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.coincount = 0
        self.__elapsed_time = 0
        self.__can_spawn = True
        self.coinlist = []
        self.drag_coins = False

    def drop_coin(self, params=None):

        self.__elapsed_time += Time.get_deltatime()
        if self.__elapsed_time > 0.2 and self.coincount < 6 and self.__can_spawn == True:
            # print("dropped")
            # print(len(self.coinlist)+ 1)
            coin = GameObject("Coin")
            coin.add_component(SpriteRenderer("coinv2.png"))
            coin.add_component(CircleCollider(0.5)).collider_layer = "coin"
            coin.transform.position = self.game_object.transform.position + Vec2(-20, -100)
            coin.transform.scale.x = 20
            coin.transform.scale.y = 20
            coin.add_component(Rigidbody(20)).restitution = 0.7
            coin.get_component(Rigidbody).gravity_scale = 4
            self.__elapsed_time = 0
            self.coincount += 1
            self.coinlist.append(coin.get_component(Rigidbody))
    
    def greed(self):
        if self.drag_coins is True:
            for coin in self.coinlist:
                coin.add_impulse((self.game_object.transform.position - coin.game_object.transform.position).normalize() * 2000)
    
    def pocket(self):
        pass

    def on_collision(self, params=None):
        colliderA = params[0]
        colliderB = params[1]

        birdCollider = self.game_object.get_component(Collider)

        collider_to_test = None
        if (colliderA == birdCollider):
            collider_to_test = colliderB
        else:
            collider_to_test = colliderA
        
        for coin in self.coinlist:
            if (collider_to_test == coin.collider):
                coin.game_object.destroy()
                self.coinlist.remove(coin)
                return

        super().on_collision(params)
        
    def update(self, params=None):
        self.greed()
        super().update(params)
        

    def passive(self):
        self.drop_coin()

    def ability(self):
        self.drag_coins = True
        