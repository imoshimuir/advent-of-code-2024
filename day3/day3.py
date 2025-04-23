from typing import Generator, List, Dict
from collections import Counter
import re

def parse_file_join(file_path: str) -> list:
    with open(file_path, "r") as f:
        input = f.readlines()
        input = ''.join(input)
        return input


def get_total_for_str(string: str) -> int:
    a, b = map(int, re.findall(r'\d+', string))
    return int(a)*int(b)
    
def get_next_total_for_str2(string: str) -> Generator:
    for instruction in re.finditer(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", string):
        match instruction.group():
            case "do()":
                evaluate = True
            case "don't()":
                evaluate = False
            case _:
                if evaluate:
                    yield get_total_for_str(instruction.group())

def main() -> None:
    total = 0
    input = parse_file_join("example.txt")
    total = sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d*),(\d*)\)", input))
    print("Part One: ", total)


    evaluate = True

    total3 = 0
   
    for instruction in re.finditer(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", input):
        match instruction.group():
            case 'do()':
                evaluate = True
            case "don't()":
                evaluate = False
            case _:
                if evaluate:
                    total3 += get_total_for_str(instruction.group())

    print(sum(get_next_total_for_str2(input)))
    print("Part Two: ", total3)


if __name__ == "__main__":
    main()
