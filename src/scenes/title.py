from play_framework import scene, TextBox, SceneManager
from res import resource


@scene(resource.bg_test_png)
def title_scene(sm: SceneManager):
    title = TextBox(100, 100, 200, 50, "Hello")

    sm.show(title)

    sm.wait_key()

    sm.hide(title)

    sm.wait_key()

    return "end"
