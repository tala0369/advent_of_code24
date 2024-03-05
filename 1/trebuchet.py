
# Find calibration value of each line in input
# Calibration value found by combining first and last digit in order per line
# Return sum of all calibration values
from pathlib import Path
from typing import List
import re

FILENAME = "input.txt"

# Get file saved in same dir
def get_lines(filename: str) -> List[str]:
    p = Path(__file__).with_name(filename)
    with p.open("r") as f:
        lines = f.readlines()
    return lines

def get_calibration_val(line: str) -> int:
    digit_pattern = re.compile("\d")
    first_digit = digit_pattern.search(line).group()
    last_digit = digit_pattern.search(line[::-1]).group()
    calibration_val = int(first_digit + last_digit)
    return calibration_val
    

def get_calibration_total():
    lines = get_lines(FILENAME)
    sum = 0
    for l in lines:
        this_val = get_calibration_val(l)
        sum += this_val
    print(f"Sum of calibration vals: {sum}")
    return sum


get_calibration_total()
