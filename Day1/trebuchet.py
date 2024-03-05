from pathlib import Path
from typing import List
import re

# Find calibration value of each line in input
# Calibration value found by combining first and last digit in order per line
# Return sum of all calibration values

FILENAME = "input.txt"
DIGIT_LIST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# Get file saved in same dir
def get_lines(filename: str) -> List[str]:
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.read()
        lines = lines.splitlines()
    return lines


def digit_string_lookup(string_digit: str) -> str:
    if string_digit in DIGIT_LIST:
        val = DIGIT_LIST.index(string_digit) + 1
        return str(val)
    else:
        return string_digit


def get_calibration_val(line: str) -> int:
    pattern = r"(?=(\d|" + "|".join(s for s in DIGIT_LIST) + "))"
    digits = re.findall(pattern, line)
    first_digit = digit_string_lookup(digits[0])
    last_digit = digit_string_lookup(digits[-1])
    calibration_val = int(first_digit + last_digit)
    return calibration_val


def get_calibration_total():
    lines = get_lines(FILENAME)
    total_sum = 0
    for l in lines:
        this_val = get_calibration_val(l)
        total_sum += this_val
    print(f"Sum of calibration vals: {total_sum}")
    return total_sum


get_calibration_total()
