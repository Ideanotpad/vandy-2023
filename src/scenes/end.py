from play_framework import SceneManager, scene
from res import resource


@scene(resource.bg_end_png)
def end_scene(sm: SceneManager):
    sm.wait_key()

    return "exit"
