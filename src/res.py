from pathlib import Path
from pathtyped import *  # type: ignore
from pathtyped.lib import loader

import pygame


@loader
@extension("png|jpg")
def pygame_image_loader(_: ResourceManager, path: Path) -> pygame.Surface:
    return pygame.image.load(path)


types = """
import pygame

Surface = pygame.Surface
"""

rm = ResourceManager(
    f"resources",
    DefinitionFile(types, f"src/definition.py"),
    [remove_known_extensions(r"txt|json")],
    [Loaders.text, Loaders.json, pygame_image_loader],
)

# The file below does not exist yet
from definition import root

resource: root = rm.root  # type: ignore
