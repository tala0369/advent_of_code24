from pathlib import Path
from typing import List


# Get file saved in same dir
def get_lines(path: Path) -> List[str]:
    with path.open("r") as f:
        lines = f.read()
        lines = lines.splitlines()
    return lines
