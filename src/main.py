import sys
import os

# Fix imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from pathtyped import * # type: ignore

rm = ResourceManager(
    f"resources",
    DefinitionFile("", f"src/definition.py"),
    [remove_known_extensions(r"txt|json")],
    [Loaders.text, Loaders.json],
)

# The file below does not exist yet
from definition import root

resource: root = rm.root # type: ignore

print(resource.hello)