import import_fix  # Do not delete this
from res import resource
from play_framework import SceneManager
from scenes.end import end_scene
from scenes.title import title_scene

sm = SceneManager(
    {
        "title": title_scene,
        "end": end_scene,
    }
)


sm.run()
