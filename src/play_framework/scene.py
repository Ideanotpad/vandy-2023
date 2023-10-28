from functools import wraps
from typing import Callable
import pygame

from play_framework import SceneManager


def scene(background: pygame.Surface):
    def scene_inner(f: Callable[[SceneManager], str]):
        """
        Decorator to register a scene.
        """

        @wraps(f)
        def wrapper(sm: SceneManager):
            sm.background = background
            return f(sm)

        return wrapper

    return scene_inner
