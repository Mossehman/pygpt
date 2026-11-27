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
        self.rect = None
        self.apply_camera_scaling = True

    def before_render(self, params=None):
        camera = self.game_object.get_scene().camera
        width = self.game_object.transform.scale.x  * GameRenderer.canvas_scale
        height = self.game_object.transform.scale.y * GameRenderer.canvas_scale

        if (self.apply_camera_scaling == True):
            width *= camera.render_scale
            height *= camera.render_scale

        image = AssetLoader.load_image(self.__image_path, (width, height))
        rotated_img = pygame.transform.rotate(image, self.game_object.transform.get_render_rotation())

        pos = Vec2(-camera.game_object.transform.position.x, -camera.game_object.transform.position.y)
        render_center = pos + Vec2(GameRenderer.width / 2 * GameRenderer.canvas_scale, GameRenderer.height / 2 * GameRenderer.canvas_scale)
        renderPos = ((self.game_object.transform.get_render_pos()) * GameRenderer.canvas_scale * camera.render_scale) + render_center
        
        if (self.apply_camera_scaling == False):
            renderPos = (self.game_object.transform.get_render_pos()) * GameRenderer.canvas_scale

        self.rect = rotated_img.get_rect(center=((renderPos).to_tuple()))

        GameRenderer.enqueue_for_rendering(rotated_img, self.rect, self.layer)



    