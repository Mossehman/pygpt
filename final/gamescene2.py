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

class GameScene2(Scene):
    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        GameRenderer.set_backdrop(AssetLoader.load_image("sky1.png"))
        PhysicsManager.add_ignore_collision("coin", "default")
        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("red rabbi.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        red = my_go.add_component(Red(150, 100))
        my_go.transform.position.x = -450
        my_go.transform.position.y = 750
        my_go.transform.scale.x = 40
        my_go.transform.scale.y = 40
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2
        birdRB.kinematic = True

        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("white soldier.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        white = my_go.add_component(Whitebird(150, 100))
        my_go.transform.position.x = -500
        my_go.transform.position.y = 750
        my_go.transform.scale.x = 40
        my_go.transform.scale.y = 40
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2
        birdRB.kinematic = True


        my_go = GameObject("Test")
        my_go.add_component(SpriteRenderer("white soldier.png"))
        my_go.add_component(CircleCollider(0.5)).collider_layer = "bird"
        white2 = my_go.add_component(Whitebird(150, 100))
        my_go.transform.position.x = -550
        my_go.transform.position.y = 750
        my_go.transform.scale.x = 40
        my_go.transform.scale.y = 40
        birdRB = my_go.add_component(Rigidbody(200))
        birdRB.restitution = 0.7
        birdRB.gravity_scale = 2
        birdRB.kinematic = True


        self.camera.game_object.transform.position.y = GameRenderer.height * 0.5
        cam = self.camera.game_object.add_component(GameCamera())

        slingshot_go = GameObject("Slingshot")
        slingshot_go.add_component(SpriteRenderer("Slingshot.png"))
        slingshot_go.transform.position.x -450
        slingshot_go.transform.position.y = 750
        slingshot_go.transform.scale.x = 75
        slingshot_go.transform.scale.y = 75
        slingshot = slingshot_go.add_component(SlingshotComponent([red, white, white2], 200000))
        slingshot_go.get_component(SlingshotComponent).distance = 20
        slingshot.bird_shoot_event.add_listener(cam.set_attached_bird)
        slingshot.bird_die_event.add_listener(cam.bird_die)
        slingshot.aim_event.add_listener(cam.set_aiming)

        floor_go = GameObject("Floor")
        floor_go.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "floor"
        floor_go.transform.position.x = 500
        floor_go.transform.position.y = 850
        floor_go.transform.scale.x = 20000
        floor_go.transform.scale.y = 100

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(450, 800)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(150))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(450, 600)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(550, 800)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(550, 600)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(150))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(500, 550)
        test_block_go.transform.scale = Vec2(130, 40)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(750, 900)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(850, 900)
        test_block_go.transform.scale = Vec2(40, 100)

        # test_block_go = GameObject("Test Block")
        # test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        # test_block_go.add_component(Rigidbody(150))
        # test_block_go.add_component(SpriteRenderer("placeholder.png"))
        # test_block_go.transform.position = Vec2(800, 150)
        # test_block_go.transform.scale = Vec2(130, 40)


        test_pig = GameObject("Test Pig")
        test_pig.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "pig"
        test_pig.add_component(Rigidbody())
        test_pig.add_component(SpriteRenderer("revert.png"))
        test_pig.transform.position = Vec2(500, 500)
        test_pig.transform.scale = Vec2(40, 40)
        pig = test_pig.add_component(PowerPig(300))



        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(750, 700)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(850, 700)
        test_block_go.transform.scale = Vec2(40, 100)

        test_block_go = GameObject("Test Block")
        test_block_go.add_component(PolygonCollider(PolygonCollider.BOX()))
        test_block_go.add_component(Rigidbody(180))
        test_block_go.add_component(SpriteRenderer("placeholder.png"))
        test_block_go.transform.position = Vec2(800, 560)
        test_block_go.transform.scale = Vec2(140, 40)

        test_pig = GameObject("Test Pig")
        test_pig.add_component(PolygonCollider(PolygonCollider.BOX())).collider_layer = "pig"
        test_pig.add_component(Rigidbody())
        test_pig.add_component(SpriteRenderer("muslim pig.png"))
        test_pig.transform.position = Vec2(800, 750)
        test_pig.transform.scale = Vec2(40, 40)
        pig = test_pig.add_component(Pig(500))

        PhysicsManager.add_ignore_collision("barrier", "default")
        PhysicsManager.add_ignore_collision("barrier", "pig")
        PhysicsManager.add_ignore_collision("barrier", "bomb")
        PhysicsManager.add_ignore_collision("barrier", "coin")
        pig_manager = GameObject("Pig Manager")
        pig_manager.add_component(PigManager([pig]))

        tiling_manager = GameObject("Tiling Manager")
        tiling_manager.add_component(TilingManager(1200, "ground.png"))
        tiling_manager.transform.scale = Vec2(1200, 600)
        tiling_manager.transform.position = self.camera.game_object.transform.position + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, - (GameRenderer.height / 2 * GameRenderer.canvas_scale)) * 0.5
