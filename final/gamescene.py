from core.scene import Scene
from core.gameobject import GameObject
from core.gamerenderer import GameRenderer
from core.physicsmanager import PhysicsManager
from components.polygoncollider import PolygonCollider
from components.circlecollider import CircleCollider
from components.collider import Collider
from components.spriterenderer import SpriteRenderer
from components.rigidbody import Rigidbody
from components.transform import Transform
from components.button import Button
from utility.assetloader import AssetLoader
from utility.vec2 import Vec2

from rainier.PBird import Purple
from rainier.Wbird import Whitebird
from rainier.RBird import Red, Bird

from aaron.pig import Pig
from aaron.pigmanager import PigManager
from aaron.slingshot import SlingshotComponent
from aaron.powerpig import PowerPig
from aaron.tileablebg import TilingManager
from aaron.gamecamera import GameCamera

class GameScene(Scene):

    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        GameRenderer.set_backdrop(AssetLoader.load_image("sky1.png"))

        whiteBird = GameObject("White Bird")
        whiteBird2 = GameObject("White Bird 2")
        purpleBird = GameObject("Purple Bird")
        


        whiteBird.add_component(CircleCollider(0.5)).collider_layer = "bird"
        whiteBird.add_component(SpriteRenderer("White.png"))
        testprint = lambda p: print("No pigs")

        whiteBird.transform.position.x = -450
        whiteBird.transform.position.y = 750
        whiteBird.transform.scale.x = 40
        whiteBird.transform.scale.y = 40
        whiteBirdRB = whiteBird.add_component(Rigidbody(200))
        whiteBirdRB.restitution = 0.7
        whiteBirdRB.gravity_scale = 2
        whiteBirdRB.kinematic = True
        white = whiteBird.add_component(Whitebird(0, 0))


        whiteBird2.add_component(CircleCollider(0.5)).collider_layer = "bird"
        whiteBird2.add_component(SpriteRenderer("red rabbi.png"))
        whiteBird2.transform.position.x = -500
        whiteBird2.transform.position.y = 750
        whiteBird2.transform.scale.x = 40
        whiteBird2.transform.scale.y = 40
        whiteBirdRB2 = whiteBird2.add_component(Rigidbody(200))
        whiteBirdRB2.restitution = 0.7
        whiteBirdRB2.gravity_scale = 2
        whiteBirdRB2.kinematic = True
        white2 = whiteBird2.add_component(Red(0, 0))

        purpleBird.add_component(CircleCollider(0.5)).collider_layer = "bird"
        purpleBird.add_component(SpriteRenderer("purple banker.png"))
        purpleBird.transform.position.x = -400
        purpleBird.transform.position.y = 750
        purpleBird.transform.scale.x = 40
        purpleBird.transform.scale.y = 40
        purpleBirdRB = purpleBird.add_component(Rigidbody(200))
        purpleBirdRB.restitution = 0.7
        purpleBirdRB.gravity_scale = 2
        purpleBirdRB.kinematic = True
        purple = purpleBird.add_component(Purple(0, 0))

        self.camera.game_object.transform.position.y = GameRenderer.height * 0.5
        cam = self.camera.game_object.add_component(GameCamera())

        slingshot_go = GameObject("Slingshot")
        slingshot_go.add_component(SpriteRenderer("Slingshot.png")) 
        slingshot = slingshot_go.add_component(SlingshotComponent([purple, white, white2], 200000))
        slingshot_go.get_component(SlingshotComponent).distance = 20
        slingshot_go.transform.position.x = -400
        slingshot_go.transform.position.y = 750
        slingshot_go.transform.scale.x = 75
        slingshot_go.transform.scale.y = 75
        slingshot.bird_shoot_event.add_listener(cam.set_attached_bird)
        slingshot.bird_die_event.add_listener(cam.bird_die)
        slingshot.aim_event.add_listener(cam.set_aiming)
        


        floor_go = GameObject("Floor")
        floor_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        floor_go.transform.position.x = 500
        floor_go.transform.position.y = 850
        floor_go.transform.scale.x = 20000
        floor_go.transform.scale.y = 100



        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(200)).friction = 20
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(480, 500)
        test_block_go.transform.scale = Vec2(50, 100)

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
        test_block_go5.add_component(Rigidbody(200)).friction = 20
        test_block_go5.add_component(SpriteRenderer("placeholder.png"))
        test_block_go5.transform.position = Vec2(730, 500)
        test_block_go5.transform.scale = Vec2(50, 100)

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
        test_block_go8.transform.position = Vec2(600, 300)
        test_block_go8.transform.scale = Vec2(40, 100)
        
        test_block_go9 = GameObject("Test Block")
        test_block_go9.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go9.add_component(Rigidbody(150))
        test_block_go9.add_component(SpriteRenderer("placeholder.png"))
        test_block_go9.transform.position = Vec2(480, 300)
        test_block_go9.transform.scale = Vec2(40, 100)

        test_block_go10 = GameObject("Test Block")
        test_block_go10.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go10.add_component(Rigidbody(150))
        test_block_go10.add_component(SpriteRenderer("placeholder.png"))
        test_block_go10.transform.position = Vec2(720, 300)
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
        test_pig.add_component(SpriteRenderer("Pig.png"))
        test_pig.transform.position = Vec2(670, 200)
        test_pig.transform.scale = Vec2(40, 40)
        pig = test_pig.add_component(PowerPig(500))


        PhysicsManager.add_ignore_collision("barrier", "default")
        pig_manager = GameObject("Pig Manager")
        pig_manager.add_component(PigManager([pig])).on_pigs_dead.add_listener(testprint)

        tiling_manager = GameObject("Tiling Manager")
        tiling_manager.add_component(TilingManager(1200, "ground.png"))
        tiling_manager.transform.scale = Vec2(1200, 600)
        tiling_manager.transform.position = self.camera.game_object.transform.position + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, - (GameRenderer.height / 2 * GameRenderer.canvas_scale)) * 0.5



        

        