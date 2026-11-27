from core.scene import Scene
from core.gameobject import GameObject
from test.print_component import PrintComponent
from components.spriterenderer import SpriteRenderer
from components.polygoncollider import PolygonCollider
from components.collider import Collider
from components.circlecollider import CircleCollider
from components.rigidbody import Rigidbody
from test.testmovement import TestMovement
from utility.vec2 import Vec2
from rainier.bomb import Bomb
from core.gamerenderer import GameRenderer
from utility.assetloader import AssetLoader
from rainier.RBird import Red
from rainier.Wbird import Whitebird
from rainier.PBird import Purple
from rainier.coin import Coin

class TestScene(Scene):
    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        GameRenderer.set_backdrop(AssetLoader.load_image("bg1.png"))
        purple = GameObject("Purple")
        purple.add_component(SpriteRenderer("purple banker.png"))
        purple.add_component(Purple(10, 10))
        purple.transform.position = Vec2(500, 200)
        purple.add_component(Purple(500, 200))
        purple.transform.scale.x = 100
        purple.transform.scale.y = 100
        purple.add_component(Rigidbody()).enable_gravity = False
        purple.transform.rotation = 180
        purple.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        purple.add_component(Rigidbody()).kinematic = True



        my_go2 = GameObject("Test2")
        my_go2.add_component(SpriteRenderer("child bomb.png"))
        my_go2.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        my_go2.transform.position.x += 1000
        my_go2.transform.position.y += 500
        my_go2.transform.scale.x = 1000
        my_go2.transform.scale.y = 100



        my_go3 = GameObject("Test3")
        my_go3.add_component(Coin(10))
        my_go3.transform.position.x += 950
        my_go3.transform.position.y -= 50
        my_go3.transform.scale.x = 100
        my_go3.transform.scale.y = 100




        # my_go4 = GameObject("Test4")
        # my_go4.add_component(SpriteRenderer("child bomb.png"))
        # my_go4.add_component(PolygonCollider(PolygonCollider.BOX())).show_collider = True
        # my_go4.get_component(Collider).trigger = False
        # my_go4.transform.position.x += 700
        # my_go4.transform.position.y -= 50
        # my_go4.transform.scale.x = 100
        # my_go4.transform.scale.y = 300
        # my_go4.add_component(Rigidbody(5)).restitution = 0.5
        # my_go4.get_component(Rigidbody).gravity_scale = 2

        

        