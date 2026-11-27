from core.scene import Scene
from core.gameobject import GameObject
from core.gamerenderer import GameRenderer
from core.scenemanager import SceneManager
from components.polygoncollider import PolygonCollider
from components.circlecollider import CircleCollider
from components.collider import Collider
from components.spriterenderer import SpriteRenderer
from components.rigidbody import Rigidbody
from components.transform import Transform
from components.button import Button
from utility.assetloader import AssetLoader
from utility.vec2 import Vec2
import utility.gamerunning as gamerunning 

from rainier.PBird import Purple
from rainier.Wbird import Whitebird
from rainier.RBird import Red, Bird

from aaron.pig import Pig
from aaron.slingshot import SlingshotComponent
from aaron.hovereffect import HoverEffect
from aaron.screenratio import ScreenRatio

from final.gamescene import GameScene

class StartScene(Scene):

    def __init__(self, name):
        super().__init__(name)

    def on_load(self):
        GameRenderer.set_backdrop(AssetLoader.load_image("bg4.png"))
        startButton = GameObject("Start Button")
        quitButton = GameObject("Quit Button")

        startButton.add_component(SpriteRenderer("placeholder.png")).apply_camera_scaling = False

        w, h = GameRenderer.width, GameRenderer.height

        startButton.transform.position = Vec2(w/2, h/2)
        startButton.transform.scale.x = 200
        startButton.transform.scale.y = 100
        
        hover = startButton.add_component(HoverEffect(1.2, 0.3))
        btn = startButton.add_component(Button())
        startButton.add_component(ScreenRatio())
        btn.on_hover_enter.add_listener(hover.on_hover_enter)
        btn.on_hover_exit.add_listener(hover.on_hover_exit)
        btn.on_click.add_listener(lambda p : SceneManager.load_scene(GameScene("Game")))




        quitButton.add_component(SpriteRenderer("placeholder.png")).apply_camera_scaling = False

        w, h = GameRenderer.width, GameRenderer.height

        quitButton.transform.position = Vec2(w/2, h * 3/4)
        quitButton.transform.scale.x = 150
        quitButton.transform.scale.y = 50
        
        hover = quitButton.add_component(HoverEffect(1.2, 0.3))
        btn = quitButton.add_component(Button())
        quitButton.add_component(ScreenRatio())
        btn.on_hover_enter.add_listener(hover.on_hover_enter)
        btn.on_hover_exit.add_listener(hover.on_hover_exit)
        btn.on_click.add_listener(self.quit)

    def quit(self, params=None):
        print("Quit!")
        gamerunning.is_game_running = False

        