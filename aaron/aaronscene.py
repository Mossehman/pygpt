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
from core.physicsmanager import PhysicsManager
from aaron.slingshot import SlingshotComponent
from aaron.pig import Pig


class AaronScene(Scene):
    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        
        GameRenderer.set_backdrop(AssetLoader.load_image("bg2.png"))
        my_go = GameObject("Test3")
        my_go.add_component(SpriteRenderer("purple banker.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        my_go.add_component(Purple(150, 100))
        my_go.transform.position.x += 150
        my_go.transform.position.y = 100
        my_go.transform.scale.x = 25
        my_go.transform.scale.y = 25
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2


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



        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(150))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(450, 500)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go2 = GameObject("Test Block")
        test_block_go2.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go2.add_component(Rigidbody(150))
        test_block_go2.add_component(SpriteRenderer("placeholder.png"))
        test_block_go2.transform.position = Vec2(550, 500)
        test_block_go2.transform.scale = Vec2(40, 100)

        test_block_go3 = GameObject("Test Block")
        test_block_go3.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go3.add_component(Rigidbody(150))
        test_block_go3.add_component(SpriteRenderer("placeholder.png"))
        test_block_go3.transform.position = Vec2(500, 350)
        test_block_go3.transform.scale = Vec2(100, 20)

        test_block_go4 = GameObject("Test Block")
        test_block_go4.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go4.add_component(Rigidbody(150))
        test_block_go4.add_component(SpriteRenderer("placeholder.png"))
        test_block_go4.transform.position = Vec2(650, 500)
        test_block_go4.transform.scale = Vec2(40, 100)

        test_block_go5 = GameObject("Test Block")
        test_block_go5.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go5.add_component(Rigidbody(150))
        test_block_go5.add_component(SpriteRenderer("placeholder.png"))
        test_block_go5.transform.position = Vec2(750, 500)
        test_block_go5.transform.scale = Vec2(40, 100)

        test_block_go6 = GameObject("Test Block")
        test_block_go6.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go6.add_component(Rigidbody(150))
        test_block_go6.add_component(SpriteRenderer("placeholder.png"))
        test_block_go6.transform.position = Vec2(600, 350)
        test_block_go6.transform.scale = Vec2(100, 20)

        test_block_go7 = GameObject("Test Block")
        test_block_go7.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go7.add_component(Rigidbody(150))
        test_block_go7.add_component(SpriteRenderer("placeholder.png"))
        test_block_go7.transform.position = Vec2(700, 350)
        test_block_go7.transform.scale = Vec2(100, 20)
        


        test_block_go8 = GameObject("Test Block")
        test_block_go8.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go8.add_component(Rigidbody(150))
        test_block_go8.add_component(SpriteRenderer("placeholder.png"))
        test_block_go8.transform.position = Vec2(600, 250)
        test_block_go8.transform.scale = Vec2(40, 100)
        
        test_block_go9 = GameObject("Test Block")
        test_block_go9.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go9.add_component(Rigidbody(150))
        test_block_go9.add_component(SpriteRenderer("placeholder.png"))
        test_block_go9.transform.position = Vec2(480, 250)
        test_block_go9.transform.scale = Vec2(40, 100)

        test_block_go10 = GameObject("Test Block")
        test_block_go10.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go10.add_component(Rigidbody(150))
        test_block_go10.add_component(SpriteRenderer("placeholder.png"))
        test_block_go10.transform.position = Vec2(720, 250)
        test_block_go10.transform.scale = Vec2(40, 100)



        
        test_block_go7 = GameObject("Test Block")
        test_block_go7.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go7.add_component(Rigidbody(150))
        test_block_go7.add_component(SpriteRenderer("placeholder.png"))
        test_block_go7.transform.position = Vec2(530, 200)
        test_block_go7.transform.scale = Vec2(150, 20)

        test_block_go7 = GameObject("Test Block")
        test_block_go7.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go7.add_component(Rigidbody(150))
        test_block_go7.add_component(SpriteRenderer("placeholder.png"))
        test_block_go7.transform.position = Vec2(670, 200)
        test_block_go7.transform.scale = Vec2(150, 20)



        test_pig = GameObject("Test Pig")
        test_pig.add_component(CircleCollider(0.5))
        test_pig.add_component(Rigidbody())
        test_pig.add_component(PowerPig())
        test_pig.add_component(SpriteRenderer("Pig.png"))
        test_pig.transform.position = Vec2(670, 200)
        test_pig.transform.scale = Vec2(40, 40)
        test_pig.add_component(Pig())


