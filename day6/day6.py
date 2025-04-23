

from typing import List


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [list(line.strip()) for line in f]



def main() -> None:
    input = parse_file("input.txt")

    rows = len(input)
    cols = len(input[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
 
    for col in range(cols):
        for row in range(rows):
            if input[row][col] == "<":
                print("Found <, row: ", row, "col: ", col)
                start_position = (row, col)
                start_direction_idx = 3
                break
            if input[row][col] == ">":
                print("Found >, row: ", row, "col: ", col)
                start_position = (row, col)
                start_direction_idx = 1
                break
            if input[row][col] == "^":
                print("Found ^, row: ", row, "col: ", col)
                start_position = (row, col)
                start_direction_idx = 0
                break
            if  input[row][col] == "v":
                print("Found v, row: ", row, "col: ", col)
                start_position = (row, col)
                start_direction_idx = 2
                break
    print(start_position[0])
    position = start_position

    direction_idx = start_direction_idx
    counter = 1
    # mark the starting position
    input[position[0]][position[1]] = "X"
    blank_grid = input
    blank_grid = [row[:] for row in input]
    possible_obstacle_positions = []
    while (0 <= position[0] < rows) and (0 <= position[1] < cols):
        direction = directions[direction_idx]
        # need to move up 
        if (position[0] + direction[0] < 0) or (position[0] + direction[0] >= rows):
            break
        if (position[1] + direction[1] < 0) or (position[1] + direction[1] >= cols):
            break

        next_position = (position[0] + direction[0], position[1] + direction[1])

        if input[next_position[0]][next_position[1]] == "#":
            # need to turn right
            if direction_idx == 3:
                direction_idx = 0
            else:
                direction_idx+=1
        else:
            if input[next_position[0]][next_position[1]] != "X":
                input[next_position[0]][next_position[1]] = "X"
                possible_obstacle_positions.append(next_position)
                counter+=1
                # print("Marking position: ", next_position)

            position = next_position

    print("Counter: ", counter)

    total_infinite_loops = 0
    
    for possible_obstacle_position in possible_obstacle_positions:
        grid = [row[:] for row in blank_grid]
        grid[possible_obstacle_position[0]][possible_obstacle_position[1]] = "#"

        direction_idx = start_direction_idx
        position = start_position

        visited_positions = {}

        while (0 <= position[0] < rows) and (0 <= position[1] < cols):
            direction = directions[direction_idx]
            # need to move up 
            if (position[0] + direction[0] < 0) or (position[0] + direction[0] >= rows):
                break
            if (position[1] + direction[1] < 0) or (position[1] + direction[1] >= cols):
                break

            next_position = (position[0] + direction[0], position[1] + direction[1])

            if grid[next_position[0]][next_position[1]] == "#":
                # need to turn right
                if direction_idx == 3:
                    direction_idx = 0
                else:
                    direction_idx+=1
            else:
                if grid[next_position[0]][next_position[1]] != "X":
                    grid[next_position[0]][next_position[1]] = "X"
                    visited_positions[next_position] = [direction]
                else:
                    if next_position in visited_positions:
                        saved_directions = visited_positions[next_position]
                        if direction in saved_directions:
                            total_infinite_loops += 1
                            print(possible_obstacle_position)
                            break
                        visited_positions[next_position].append(direction)
                position = next_position

    print("Total infinite loops: ", total_infinite_loops)
    # for row in blank_grid:
    #     print(row)

if __name__ == "__main__":
    main()
