from utils import utils
from pathlib import Path
from typing import List
from collections import defaultdict
from functools import reduce


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


def is_game_valid(max_count: dict[int], results: List[dict]) -> bool:
    for round in results:
        for color, count in round.items():
            if count > max_count[color]:
                return False
    return True


def get_games() -> List[str]:
    path = Path(__file__).with_name("input.txt")
    lines = utils.get_lines(path)
    all_games = [get_game_from_line(l) for l in lines]
    return all_games


def part_one() -> int:
    max_count = {"red": 12, "green": 13, "blue": 14}
    all_games = get_games()
    id_sum = 0
    for game in all_games:
        if is_game_valid(max_count, game["results"]):
            id_sum += game["id"]
    return id_sum


def get_max_values(results: List[dict]):
    max_values = defaultdict(int)
    for round in results:
        for color, count in round.items():
            max_values[color] = max(count, max_values[color])
    return max_values


def part_two():
    all_games = get_games()
    power_sum = 0
    for game in all_games:
        max_values = get_max_values(game["results"])
        power = reduce(lambda x, y: x * y, max_values.values())
        power_sum += power
    return power_sum


print(part_one())
print(part_two())
