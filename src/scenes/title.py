from play_framework import scene, TextBox, SceneManager
from res import resource

from characters import stick


@scene(resource.bg_test_png)
def title_scene(sm: SceneManager):
    title = TextBox(100, 100, 200, 50, "Hello")

    sm.show(title)

    sm.wait_key()

    sm.show(stick)

    sm.wait_key()

    stick.set_state("explain")
    title._text = "Click again to start"

    sm.wait_key()

    sm.hide(title)

    return "end"
