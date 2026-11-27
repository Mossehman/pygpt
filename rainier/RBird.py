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
from core.eventhandler import AppEvent

class Bird(Component):
    def __init__(self, x, y):
        super().__init__(True)
        self.start_position = Vec2(x, y)
        self.launched = False # bird not launched yet
        self.used_ability = False
        self.alive = True
        self.death_event = AppEvent()
    
    def awake(self, params=None):
        self.rb = self.game_object.get_component(Rigidbody) # Cache the rigidbody

       
    def reset_pos(self):
        attached_gameobject = self.game_object # -> This gets us the game object that contains this component
        transform = attached_gameobject.transform
        transform.position = self.start_position
        self.my_pos = transform.position

    def update(self, params=None):

        if self.launched and self.used_ability == False:
            self.passive()
            if MouseManager.mouse_down():
                self.ability()
                self.used_ability = True

    def on_dead(self):
        self.death_event.invoke()
        return

    # for any bird passive ability
    def passive(self):
        return

    # for the bird click skill
    def ability(self):
        return

    def on_collision(self, params=None):
        if self.launched == True:
            self.death_event.invoke()
            self.game_object.destroy()

    
class Red(Bird):
    def __init__(self, x, y):
        super().__init__(x, y)

    def start(self, params=None):
        pass
        # red = GameObject("Red")
        # red.add_component(SpriteRenderer("red rabbi.png"))
        # red.add_component(CircleCollider(0.5)).show_collider = True
        # red.transform.position = self.game_object.transform.position
        # red.transform.scale.x = 100
        # red.transform.scale.y = 100
        # red.add_component(Rigidbody()).restitution = 0.8