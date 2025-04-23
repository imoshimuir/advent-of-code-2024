from typing import List
import re
import matplotlib.pyplot as plt 
import scipy.stats


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [line.strip().split(" ") for line in f]

def get_safety_factors(seconds: int, input: List[str], Print: bool) -> List[int]: 
    width = 101
    tall = 103

    grid = [["." for _ in range(width)] for _ in range(tall)]
    safety_factors = []
    positions = {}
    for i in range(seconds):
        for j, line in enumerate(input):
            if j not in positions:
                positions[j] = position = [
                    int(x) for x in re.findall(r"[+-]?\d+", line[0])
                ]
            else:
                position = positions[j]
            velocity = [int(x) for x in re.findall(r"[+-]?\d+", line[1])]

            # create grid of points
            # grid = [["." for _ in range(width)] for _ in range(tall)]
            # # y, x
            # grid[position[1]][position[0]] = "1"
            
            # move the robot to the next position

            if grid[position[1]][position[0]] != ".":
                num_robots = int(grid[position[1]][position[0]])
                if num_robots == 1:
                    grid[position[1]][position[0]] = "."
                else:
                    grid[position[1]][position[0]] = num_robots - 1
            
            position[0] += velocity[0]
            position[1] += velocity[1]
            

            position[1] = position[1] % len(grid)
            position[0] = position[0] % len(grid[0])
            # grid[position[1]][position[0]] = 1


            if grid[position[1]][position[0]] != ".":
                num_robots = int(grid[position[1]][position[0]])
                grid[position[1]][position[0]] = num_robots + 1
            else:
                grid[position[1]][position[0]] = 1
        

        
        # split grid into 4 quadrants
        total_grid_1 = 0
        for row in grid[:len(grid)//2]:
            for j in row[:len(row)//2]:
                if j != ".":
                    total_grid_1 += j

        total_grid_2 = 0
        for row in grid[:len(grid)//2]:
            for j in row[len(row)//2 + 1:]:
                if j != ".":
                    total_grid_2 += j
        total_grid_3 = 0
        for row in grid[len(grid)//2 + 1:]:
            for j in row[:len(row)//2]:
                if j != ".":
                    total_grid_3 += j
        total_grid_4 = 0
        for row in grid[len(grid)//2 + 1:]:
            for j in row[len(row)//2 + 1:]:
                if j != ".":
                    total_grid_4 += j
        safety_factor = total_grid_1 * total_grid_2 * total_grid_3 * total_grid_4

        # print(safety_factor)
        safety_factors.append(safety_factor)

        # check if grid contains only 1s or "."s
        # if so, print the grid
        if all(all((cell == 1 or cell == ".") for cell in row) for row in grid):
            print(i)
            for row in grid:
                print("".join(str(cell) for cell in row))

            

    
    if Print:
        for row in grid:
            print("".join(str(cell) for cell in row))

    return safety_factors

def main():
    input = parse_file("input.txt")
    

    safety_factors = get_safety_factors(10000, input, False)
    print(safety_factors[len(safety_factors) - 1])
    #  find lowest index of safety factor

    print(safety_factors.index(min(safety_factors)))
    # plot the safety factors
    print(min(safety_factors))

    plt.plot(safety_factors[7000:8500])
    plt.show()

    # safety_factor = get_safety_factor(936, input, True)
    # print(safety_factor)

if __name__ == "__main__":
    main()