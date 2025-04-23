from typing import List


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [x for x in f.read().split("\n\n")]


def main() -> None:
    part1, part2 = parse_file("input.txt")

    comparisons = [
        (int(x), int(y)) for x, y in [part.split("|") for part in part1.split("\n")]
    ]

    rows = [[int(num) for num in part.split(",")] for part in part2.split("\n")]

    part_one_sum = 0
    part_2_sum = 0
    for row in rows:
        in_order = True
        for i, j in comparisons:
            if i in row and j in row:
                idx_i = row.index(i)
                idx_j = row.index(j)
                if idx_i > idx_j:
                    in_order = False
                    break
        if in_order:
            middle_index = len(row) // 2
            part_one_sum += row[middle_index]

        if not in_order:
            # reorder the row based on the comparisons
            while not in_order:
                in_order = True
                for i, j in comparisons:
                    if i in row and j in row:
                        idx_i = row.index(i)
                        idx_j = row.index(j)
                        if idx_i > idx_j:
                            in_order = False
                            row[idx_i], row[idx_j] = row[idx_j], row[idx_i]
            middle_index = len(row) // 2
            part_2_sum += row[middle_index]

    print(part_one_sum)
    print(part_2_sum)


if __name__ == "__main__":
    main()
