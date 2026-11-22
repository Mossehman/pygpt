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
        my_go.transform.position.y += 500
        my_go.transform.scale.x = 1000
        my_go.transform.scale.y = 100
        my_go.transform.rotation = 180
        my_go.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        my_go.add_component(Rigidbody()).kinematic = True

        my_go2 = GameObject("Test2")
        my_go2.add_component(SpriteRenderer("Red.png"))
        my_go2.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        my_go2.transform.position.x += 1000
        my_go2.transform.position.y += 100
        my_go2.transform.scale.x = 100
        my_go2.transform.scale.y = 100
        my_go2.add_component(Rigidbody()).restitution = 0.5


        my_go3 = GameObject("Test3")
        my_go3.add_component(SpriteRenderer("Red.png"))
        my_go3.add_component(CircleCollider(0.5)).show_collider = True
        my_go3.transform.position.x += 950
        my_go3.transform.position.y -= 50
        my_go3.transform.scale.x = 100
        my_go3.transform.scale.y = 100
        my_go3.add_component(Rigidbody()).restitution = 0
        my_go3.get_component(Rigidbody).gravity_scale = 2



        my_go4 = GameObject("Test4")
        my_go4.add_component(SpriteRenderer("Red.png"))
        my_go4.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        my_go4.transform.position.x += 700
        my_go4.transform.position.y -= 50
        my_go4.transform.scale.x = 100
        my_go4.transform.scale.y = 300
        my_go4.add_component(Rigidbody(5)).restitution = 1
        my_go4.get_component(Rigidbody).gravity_scale = 2

        