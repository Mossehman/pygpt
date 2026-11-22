from pathlib import Path
import pygame

# Helper class for loading game assets
class AssetLoader:
    image_cache = {}
    assets_folder = "assets" # This is so we can change the assets at runtime ;)
    def __init__(self):
        return
    
    @staticmethod
    def load_image(name, size=None):
        assets_dir = Path(__file__).resolve().parent.parent / AssetLoader.assets_folder
        path = assets_dir / name
        if (path.is_file() == False):
            raise FileNotFoundError(path) # If file doesn't even exist, throw an error (shld change this to load a placeholder asset ngl)
        
        image = None
        filepath = str(path)
        if (filepath not in AssetLoader.image_cache):
            image = pygame.image.load(filepath).convert_alpha() # Load the image if not in cache
            AssetLoader.image_cache[filepath] = image # Cache the images when needed, prevents the need for an additional file read from disk
        else:
            image = AssetLoader.image_cache[filepath] # if already in cache, just read image from there

        # Resize image as per needed
        if (size is not None):
            return pygame.transform.smoothscale(image, size)
        return image
        
