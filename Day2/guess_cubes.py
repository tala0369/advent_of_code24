from utils import utils
from pathlib import Path
from typing import List


def get_game_from_line(line: str) -> dict:
    game_id, rounds_raw = line.split(": ")
    id_num = int(game_id.split(" ")[-1])

    rounds = [r.split(", ") for r in rounds_raw.split("; ")]
    results = []
    for result_raw in rounds:
        these_results = {}
        for pick in result_raw:
            count, color = pick.split(" ")
            these_results[color] = int(count)
        results.append(these_results)
    return {"id": id_num, "results": results}


def is_game_valid(max_count, results):
    for round in results:
        for color, count in round.items():
            if count > max_count[color]:
                return False
    return True


def get_games() -> List[str]:
    path = Path(__file__).with_name("input.txt")
    lines = utils.get_lines(path)
    return lines


def part_one():
    max_count = {"red": 12, "green": 13, "blue": 14}
    all_games = get_games()
    id_sum = 0
    for game_line in all_games:
        this_game = get_game_from_line(game_line)
        if is_game_valid(max_count, this_game["results"]):
            id_sum += this_game["id"]
    return id_sum


print(part_one())
