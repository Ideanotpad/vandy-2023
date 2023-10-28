from functools import wraps
from typing import Any, Callable
import pygame


class SceneManager:
    def __init__(self, scenes: dict[str, Callable[["SceneManager"], str]]):
        self.scenes = scenes
        self.background: pygame.Surface = None  # type: ignore

        self.clock = pygame.time.Clock()

        self.objects = pygame.sprite.Group()

    def wait_key(self):
        """
        Wait for a key to be pressed.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    return event.key
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return event.button
                self._proc_scene(event)

            self.clock.tick(60)

    def wait(self, seconds: float):
        """
        Wait for a certain amount of seconds.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self._proc_scene(event)

            seconds -= self.clock.tick(60) / 1000

            if seconds <= 0:
                return

    def show(self, sprite: pygame.sprite.Sprite):
        """
        Show a sprite on the screen.
        """
        self.objects.add(sprite)

    def hide(self, sprite: pygame.sprite.Sprite):
        """
        Hide a sprite from the screen.
        """
        self.objects.remove(sprite)

    def _proc_scene(self, event):
        """
        Internal function that is called on top of a wait to update current objects to a screen.
        """
        # Background update
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        # Sprites update
        self.objects.update(event)
        self.objects.draw(pygame.display.get_surface())

        # Flip buffer
        pygame.display.flip()

    def run(self, scene_name: str | None = None):
        """
        Main blocking loop. Entrypoint of the program
        """

        pygame.init()

        scene = self.scenes[scene_name or [*self.scenes][0]]

        pygame.display.set_mode((1920, 1080))

        self.screen = pygame.display.get_surface()

        while True:
            scene_name = scene(self)

            if scene_name == "exit":
                pygame.quit()
                return

            scene = self.scenes[scene_name]
