from typing import List, Dict
from collections import Counter


def parse_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        return [[int(i) for i in line.split()] for line in f]

def is_line_safe(line: List[int]) -> bool:
    safe = True
    # for each element try removing one 
    ascending = False if line[1] - line[0] < 0 else True
    for (index, num) in enumerate(line[:-1]):
        diff = num - line[index + 1]
        if diff == 0 or diff > 3 or diff < -3:
            safe = False
            break
        elif (ascending and diff > 0) or (not ascending and diff < 0):
            safe = False
            break
    return safe

def main() -> None:

    safe_count = 0
    for line in parse_file("example.txt"):
        safe = is_line_safe(line)
        if safe:
            safe_count += 1
            continue
        
        removing_one_makes_safe = False
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            line_safe = is_line_safe(new_line)
            if line_safe:
                removing_one_makes_safe = True
            
        if removing_one_makes_safe:
            safe_count += 1

    
    print(safe_count)


if __name__ == "__main__":
    main()
