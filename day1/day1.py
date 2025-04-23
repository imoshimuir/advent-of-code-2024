from typing import List, Dict
from collections import Counter

def parse_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        return [[int(i) for i in line.split()] for line in f]



def main() -> None:
    list1: List[int] = []
    list2: List[int] = []

    for line in parse_file("day1.txt"):
        list1.append(line[0])
        list2.append(line[1])

    print(
        "Part 1 Solution: Total distance: ",
        sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2))),
    )

    count_of_l2 = Counter(list2)

    print("Part 2 Solution: Similarity score: ", sum(i * count_of_l2[i] for i in list1))

if __name__ == "__main__":
    main()
