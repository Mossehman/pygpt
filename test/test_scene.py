from core.scene import Scene
from core.gameobject import GameObject
from test.print_component import PrintComponent
from components.spriterenderer import SpriteRenderer
from components.polygoncollider import PolygonCollider
from components.circlecollider import CircleCollider
from components.rigidbody import Rigidbody
from test.testmovement import TestMovement
from utility.vec2 import Vec2

class TestScene(Scene):
    def __init__(self, name):
        super().__init__(name)

    def on_load(self):

        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("Red.png"))
        my_go.add_component(TestMovement(50))
        my_go.transform.position.x += 1000
        my_go.transform.position.y += 300
        my_go.transform.scale.x = 100
        my_go.transform.scale.y = 100
        my_go.transform.rotation = 180
        my_go.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        my_go.add_component(Rigidbody()).kinematic = True

        my_go2 = GameObject("Test2")
        my_go2.add_component(SpriteRenderer("Red.png"))
        my_go2.add_component(CircleCollider(0.5)).show_collider = True
        my_go2.transform.position.x += 1000
        my_go2.transform.position.y += 100
        my_go2.transform.scale.x = 100
        my_go2.transform.scale.y = 100
        my_go2.add_component(Rigidbody()).restitution = 0.5