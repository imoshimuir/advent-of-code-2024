import itertools
import re
from typing import List


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [list(line.strip()) for line in f]


def main() -> None:
    input = parse_file("input.txt")
    print(input)

    rows = len(input)
    cols = len(input[0])

    pattern = r"[0-9a-zA-Z]"

    antenna_positions = {}

    for row in range(rows):
        for col in range(cols):
            print(input[row][col], end="")
            if re.match(pattern, input[row][col]):
                # print("Matched: ", input[row][col])
                antenna = input[row][col]
                if antenna not in antenna_positions:
                    antenna_positions[antenna] = [(row, col)]
                else:
                    antenna_positions[antenna].append((row, col))

        print()

    antinode_locations_part1 = set()
    antinode_locations_part2 = set()
    total_antennas = 0
    for antenna, positions in antenna_positions.items():
        if len(positions) > 2:
            total_antennas += len(positions)
        combinations = list(itertools.combinations(positions, 2))
        for pos1, pos2 in combinations:
            # distance between two points
            print(pos2, pos1)
            horizontal_distance = pos1[1] - pos2[1]
            vertical_distance = pos1[0] - pos2[0]
            # Part 1

        
            if (0 <= pos1[0] + vertical_distance < rows and 0 <= pos1[1] + horizontal_distance < cols):
                antinode_location = (
                    pos1[0] + vertical_distance,
                    pos1[1] + horizontal_distance,
                )
                antinode_locations_part1.add(antinode_location)

            if  (0 <= (pos2[0] - vertical_distance) < rows and 0 <= pos2[1] - horizontal_distance < cols):
                antinode2_location = (
                    pos2[0] - vertical_distance,
                    pos2[1] - horizontal_distance,
                )

                antinode_locations_part1.add(antinode2_location)
            
            # Part 2
            start_position = pos1

            while (
                0 <= start_position[0] + vertical_distance < rows
                and 0 <= start_position[1] + horizontal_distance < cols
            ):

                x = start_position[0] + vertical_distance
                y = start_position[1] + horizontal_distance
                antinode_location = (
                    x,
                    y,
                )
                if not re.match(pattern, input[x][y]):
                    antinode_locations_part2.add(antinode_location)
                start_position = antinode_location


            start_position = pos2

            while (
                0 <= start_position[0] - vertical_distance < rows
                and 0 <= start_position[1] - horizontal_distance < cols
            ):
                x = start_position[0] - vertical_distance
                y = start_position[1] - horizontal_distance
                antinode_location = (
                    x,
                    y,
                )
                if not re.match(pattern, input[x][y]):
                    antinode_locations_part2.add(antinode_location)
                start_position = antinode_location
                


            # print(
            #     "Antenna: ",
            #     antenna,
            #     "Antinode1: ",
            #     antinode1_location,
            #     "Antinode2: ",
            #     antinode2_location,
            # )
    # for row in range(rows):
    #     for col in range(cols):
    #         if (row, col) in antinode_locations_part1:
    #             print("#", end="")
    #         else:
    #             print(input[row][col], end="")
    #     print()

    for row in range(rows):
        for col in range(cols):
            if (row, col) in antinode_locations_part2:
                if re.match(pattern, input[row][col]):
                    print(input[row][col], end="")
                else:
                    print("#", end="")
            else:
                print(input[row][col], end="")
        print()

    print("Part 1: ", len(antinode_locations_part1))
    print(total_antennas)
    print("Part 2: ", len(antinode_locations_part2) + total_antennas)

if __name__ == "__main__":
    main()
