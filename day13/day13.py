from typing import List
import re
from decimal import Decimal


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [x for x in f.read().split("\n\n")]


def extract_numbers(str: str) -> List[int]:
    numbers = re.findall(r"[+-]?\d+", str)
    return [int(num) for num in numbers]


def main() -> None:
    input = parse_file("input.txt")
    total_tokens = 0
    total_tokens_part_2 = 0
    for puzzle in input:
        parts = puzzle.split("\n")
        button_a = extract_numbers(parts[0])
        button_b = extract_numbers(parts[1])
        point = extract_numbers(parts[2])
    # rearranged simulataneous equations
        a = (button_b[0] * point[1] - button_b[1] * point[0]) / (
            -button_b[1] * button_a[0] + button_b[0] * button_a[1]
        )
        b = (point[0] - button_a[0] * a) / button_b[0]
        print(a,b)
       
        if a.is_integer() and b.is_integer():
            tokens = a * 3 + b 
            total_tokens += tokens
            print(tokens)

        # part 2
        part_2_point = [(10000000000000 + num) for num in point]
        print(part_2_point)

        a = (button_b[0] * part_2_point[1] - button_b[1] * part_2_point[0]) / (
            -button_b[1] * button_a[0] + button_b[0] * button_a[1]
        )
        b = (part_2_point[0] - button_a[0] * a) / button_b[0]
        if a.is_integer() and b.is_integer():
            tokens = a * 3 + b 
            total_tokens_part_2 += tokens
            print(total_tokens_part_2)
        
    print(total_tokens)
    print(total_tokens_part_2)

if __name__ == "__main__":
    main()
