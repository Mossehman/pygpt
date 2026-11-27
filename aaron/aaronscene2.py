from core.scene import Scene
from core.gameobject import GameObject
from test.print_component import PrintComponent
from components.spriterenderer import SpriteRenderer
from components.polygoncollider import PolygonCollider
from components.collider import Collider
from components.circlecollider import CircleCollider
from components.rigidbody import Rigidbody
from utility.vec2 import Vec2
from core.gamerenderer import GameRenderer
from utility.assetloader import AssetLoader
from rainier.RBird import Red
from rainier.Wbird import Whitebird
from rainier.PBird import Purple
from rainier.coin import Coin
from aaron.powerpig import PowerPig

from core.time import Time

from aaron.slingshot import SlingshotComponent
from aaron.pig import Pig

class AaronScene2(Scene):
    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        slingshot_go = GameObject("Slingshot")
        slingshot_go.add_component(SpriteRenderer("Slingshot.png"))
        slingshot_go.add_component(SlingshotComponent(200000)).attached_body = my_go.get_component(Rigidbody)
        slingshot_go.get_component(SlingshotComponent).attached_bird = my_go.get_component(Purple)
        slingshot_go.get_component(SlingshotComponent).distance = 20
        slingshot_go.transform.position.x += 100
        slingshot_go.transform.position.y = 420
        slingshot_go.transform.scale.x = 75
        slingshot_go.transform.scale.y = 75

        floor_go = GameObject("Floor")
        floor_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        floor_go.transform.position.x = 500
        floor_go.transform.position.y = 520
        floor_go.transform.scale.x = 2000
        floor_go.transform.scale.y = 100

        