import os
from pathlib import Path

b = Path(__file__)
print(b)

print(Path(__file__).parent)
b = Path(__file__).parent.parent

print(os.path.join(b, "template"))
