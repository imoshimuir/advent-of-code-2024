

from typing import List, Tuple


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return f.read().split("\n\n")

def get_grid(input: str) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid = []
    start_pos = None
    for i, line in enumerate(input.split("\n")):
        new_line = []
        for j, char in enumerate(line):
            new_line.append(char)
            if char == "@":
                start_pos = (i, j)
        grid.append(new_line)
    return grid, start_pos

def get_grid_part_two(input: str) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid = []
    start_pos = None
    for i, line in enumerate(input.split("\n")):
        new_line = ""
        for j, char in enumerate(line):
            if char == "#":
                new_line += "##"
            if char == "@":
                new_line += "@."
            if char == ".":
                new_line += ".."
            if char == "O":
                new_line += "[]"
        grid.append(list(new_line))
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "@":
                start_pos = (i, j)
    return grid, start_pos

def pass_directions(input: str) -> List[Tuple[int, int]]:
    directions = []
    for char in input:
        if char == "^":
            directions.append((-1,0))
        elif char == ">":
            directions.append((0,1))
        elif char == "v":
            directions.append((1,0))
        elif char == "<":
            directions.append((0,-1))
    return directions
    
def main() -> None:
    input = parse_file("input.txt")
    grid, start_pos = get_grid(input[0])
    print(grid, start_pos)
    directions = pass_directions(input[1])
    
    position = start_pos
    for direction in directions:
        print("Moving", direction)
        new_x = position[0] + direction[0]
        new_y = position[1] + direction[1]
        if grid[new_x][new_y] == "#":
            print("Hit wall")
        elif grid[new_x][new_y] == "O":
            # push the block go along in that direction
            print("Pushing block")
            blocks = [(new_x, new_y)]
            next_x = new_x + direction[0]
            next_y = new_y + direction[1]
            while grid[next_x][next_y] == "O":
                blocks.append((next_x, next_y))
                next_x = next_x + direction[0]
                next_y = next_y + direction[1]
            if grid[next_x][next_y] == "#":
                print("Hit wall can't push")
            else:
                print("Blocks to push", blocks)
            # move blocks by one step in direction
                for block in blocks:
                    grid[block[0] + direction[0]][block[1] + direction[1]] = "O"
                grid[position[0]][position[1]] = "."
                grid[new_x][new_y] = "@"
                position = (new_x, new_y)

        else:
            grid[position[0]][position[1]] = "."
            position = (new_x, new_y)
            grid[new_x][new_y] = "@"
        for line in grid:
            print("".join(line))
        print()
    total = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "O":
                coordinate = (100 * i) + j
                total += coordinate
    print(total)

    # Part 2

    grid, start_pos = get_grid_part_two(input[0])
    position = start_pos
    for direction in directions:
        print("Moving", direction)
        new_x = position[0] + direction[0]
        new_y = position[1] + direction[1]
        if grid[new_x][new_y] == "#":
            print("Hit wall")
        elif grid[new_x][new_y] == "[" or grid[new_x][new_y] == "]":
            # push the block go along in that direction
            # if direction is horizontal
            if direction == (0, 1) or direction == (0, -1):
                blocks = [(new_x, new_y, grid[new_x][new_y])]
                next_x = new_x + direction[0]
                next_y = new_y + direction[1]
                while grid[next_x][next_y] == "[" or grid[next_x][next_y] == "]":
                    blocks.append((next_x, next_y, grid[next_x][next_y]))
                    next_x = next_x + direction[0]
                    next_y = next_y + direction[1]
                if grid[next_x][next_y] == "#":
                    print("Hit wall can't push")
                
                else:
                    print("Blocks to push", blocks)
                # move blocks by one step in direction
                    for block in blocks:
                        grid[block[0] + direction[0]][block[1] + direction[1]] = block[2]
                    grid[position[0]][position[1]] = "."
                    grid[new_x][new_y] = "@"
                    position = (new_x, new_y)
            # if direction is vertical
            if direction == (1, 0) or direction == (-1, 0):
                # set of swaps to perform
                # branch each time box is hit


        else:
            grid[position[0]][position[1]] = "."
            position = (new_x, new_y)
            grid[new_x][new_y] = "@"
        for line in grid:
            print("".join(line))
        print()

def get_vertical_swaps(direction, grid, position):
    swaps = []
    new_x = position[0] + direction[0]
    new_y = position[1] + direction[1]
    # get both sides of the box 
    while grid[new_x][new_y] == "[" or grid[new_x][new_y] == "]":
        
    return swaps

def canMove(dir, grid, position):
    # we're doing the [ case
    new_xs = [position[0] + dir[0], position[0] + 1 + dir[1]]
    new_y = position[1] + dir[1]
    can_move = True
    for (x2, y2) in [(new_xs[0], new_y), (new_xs[1], new_y)]:
        if grid[x2][y2] == "#":
            return False
        if grid[x2][y2] in "[]":
            can_move = can_move and canMove(dir, grid, (x2, y2))
    return can_move
    
if __name__ == "__main__":
    main()