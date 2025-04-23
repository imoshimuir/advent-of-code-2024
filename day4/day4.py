from typing import Generator, List, Dict
from collections import Counter
import re


def parse_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        return [list(line.strip()) for line in f]


def part_one() -> None:
    input = parse_file("example.txt")
    print(input)
    # horizontals
    total = 0
    for chars in input:
        line = "".join(chars)
        # forwards
        total += line.count("XMAS")
        # backwards
        total += line.count("SAMX")

    # verticals
    for i in range(len(input[0])):
        vertical = "".join([line[i] for line in input])
        # forwards
        total += vertical.count("XMAS")
        # backwards
        total += vertical.count("SAMX")


    rows = len(input)
    cols = len(input[0])

    for col in range(cols):
        i, j = 0, col
        diagonal = ""
        while i < rows and j < cols:
            diagonal += input[i][j]
            i += 1
            j += 1
        total += diagonal.count("XMAS")
        total += diagonal.count("SAMX")
    # minor diagonals
    for row in range(1, rows):
        i, j = row, 0
        diagonal = ""
        while i < rows and j < cols:
            diagonal += input[i][j]
            i += 1
            j += 1
        total += diagonal.count("XMAS")
        total += diagonal.count("SAMX")

    for col in range(cols):
        i, j = 0, col
        diagonal = ""
        while i < rows and j >= 0:
            diagonal += input[i][j]
            i += 1
            j -= 1
        total += diagonal.count("XMAS")
        total += diagonal.count("SAMX")

    for row in range(1, rows):
        i, j = row, cols - 1
        diagonal = ""
        while i < rows and j >= 0:
            diagonal += input[i][j]
            i += 1
            j -= 1
        total += diagonal.count("XMAS")
        total += diagonal.count("SAMX")

    print(total)


def main() -> None:

    part_one()

    input = parse_file("example.txt")
    rows = len(input)
    cols = len(input[0])

    total = 0
    for col in range(cols):
        for row in range(rows):
            if input[row][col] == "A":

                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    continue

                # print(input[row - 1][col - 1], "-", input[row - 1][col + 1])
                # print("-", "A", "-")
                # print(input[row + 1][col - 1], "-", input[row + 1][col + 1])
                # check corners
                if (
                    input[row - 1][col - 1] == "S" and input[row + 1][col + 1] == "M"
                ) or (
                    input[row - 1][col - 1] == "M" and input[row + 1][col + 1] == "S"
                ):
                    # check for other MS
                    if (
                        input[row - 1][col + 1] == "M"
                        and input[row + 1][col - 1] == "S"
                    ) or (
                        input[row - 1][col + 1] == "S"
                        and input[row + 1][col - 1] == "M"
                    ):
                        total += 1
    print(total)

if __name__ == "__main__":
    main()
