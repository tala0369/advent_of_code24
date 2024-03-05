from utils import utils
from pathlib import Path
from typing import List


def get_games() -> List[str]:
    path = Path(__file__).with_name("input.txt")
    lines = utils.get_lines(path)
    return lines


get_games()
