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
from aaron.gamecamera import GameCamera
from aaron.tileablebg import TilingManager

class GameScene3(Scene):

    def __init__(self, name):
        super().__init__(name)

    def on_load(self):

        PhysicsManager.add_ignore_collision("coin", "default")
        GameRenderer.set_backdrop(AssetLoader.load_image("sky1.png"))
        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("purple banker.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        purple = my_go.add_component(Purple(150, 100))
        my_go.transform.position.x = -450
        my_go.transform.position.y = 750
        my_go.transform.scale.x = 40
        my_go.transform.scale.y = 40
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2
        birdRB.kinematic = True

        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("red rabbi.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        red = my_go.add_component(Red(-400, 750))
        my_go.transform.position.x = -400
        my_go.transform.position.y = 750
        my_go.transform.scale.x = 40
        my_go.transform.scale.y = 40
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2
        birdRB.kinematic = True

        floor_go = GameObject("Floor")
        floor_go.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "floor"
        floor_go.transform.position.x = 0
        floor_go.transform.position.y = 850
        floor_go.transform.scale.x = 20000
        floor_go.transform.scale.y = 100

        self.camera.game_object.transform.position.y = GameRenderer.height * 0.5
        cam = self.camera.game_object.add_component(GameCamera())

        slingshot_go = GameObject("Slingshot")
        slingshot_go.add_component(SpriteRenderer("Slingshot.png"))
        slingshot_go.transform.position.x = -400
        slingshot_go.transform.position.y = 750
        slingshot_go.transform.scale.x = 75
        slingshot_go.transform.scale.y = 75
        slingshot = slingshot_go.add_component(SlingshotComponent([red, purple], 200000))
        slingshot_go.get_component(SlingshotComponent).distance = 20
        slingshot.bird_shoot_event.add_listener(cam.set_attached_bird)
        slingshot.bird_die_event.add_listener(cam.bird_die)
        slingshot.aim_event.add_listener(cam.set_aiming)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(200000)).enable_gravity=False
        test_block_go.add_component(SpriteRenderer("stone.png"))
        test_block_go.transform.position = Vec2(450, 600)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(200000)).enable_gravity=False
        test_block_go.add_component(SpriteRenderer("stone.png"))
        test_block_go.transform.position = Vec2(550, 600)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(200000)).enable_gravity=False
        test_block_go.add_component(SpriteRenderer("stone.png"))
        test_block_go.transform.position = Vec2(500, 640)
        test_block_go.transform.scale = Vec2(100, 40)
        
        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(200000)).enable_gravity=False
        test_block_go.add_component(SpriteRenderer("stone.png"))
        test_block_go.transform.position = Vec2(500,560)
        test_block_go.transform.scale = Vec2(100, 40)
        
        test_block_go = GameObject("Thruster")
        test_block_go.add_component(SpriteRenderer("thruster.png"))
        test_block_go.transform.position = Vec2(550, 670)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Thruster")
        test_block_go.add_component(SpriteRenderer("thruster.png"))
        test_block_go.transform.position = Vec2(450, 670)
        test_block_go.transform.scale = Vec2(40, 100)

        test_pig = GameObject("Test Pig")
        test_pig.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "pig"
        test_pig.add_component(Rigidbody()).enable_gravity=False
        test_pig.add_component(SpriteRenderer("muslim pig.png"))
        test_pig.transform.position = Vec2(500, 600)
        test_pig.transform.scale = Vec2(40, 40)
        pig = test_pig.add_component(Pig(500))

        tiling_manager = GameObject("Tiling Manager")
        tiling_manager.add_component(TilingManager(1200, "ground.png"))
        tiling_manager.transform.scale = Vec2(1200, 600)
        tiling_manager.transform.position = self.camera.game_object.transform.position + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, - (GameRenderer.height / 2 * GameRenderer.canvas_scale)) * 0.5

        
        

