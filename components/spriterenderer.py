from core.component import Component
from utility.vec2 import Vec2
from core.gamerenderer import GameRenderer
from utility.assetloader import AssetLoader
import pygame


class SpriteRenderer(Component):
    def __init__(self, image_path, enabled=True):
        super().__init__(enabled)
        self.__image_path = image_path
        self.flip_x = False
        self.flip_y = False
        self.color = [255,255,255] # TODO: Add image tint
        self.layer = 0 # Image priority

    def before_render(self, params=None):
        width = self.game_object.transform.scale.x 
        height = self.game_object.transform.scale.y
        image = AssetLoader.load_image(self.__image_path, (width, height))
        rotated_img = pygame.transform.rotate(image, self.game_object.transform.rotation)
        rect = rotated_img.get_rect(center=self.game_object.transform.position.to_py())

        GameRenderer.enqueue_for_rendering(rotated_img, rect, self.layer)



    