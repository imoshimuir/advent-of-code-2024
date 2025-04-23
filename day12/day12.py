from typing import List

def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [list(line.strip()) for line in f]
    
directions = [(0,1), (1,0), (0,-1), (-1,0)]


def find_region(x,y, input, letter, nodes): 
    nodes.add((x, y))
    perimeter = 0
    num_corners = 4
    for direction in directions:
        new_x = x + direction[0]
        new_y =  y + direction[1]
        if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
            continue
        if (new_x, new_y) in nodes:
            num_corners -=1
            continue   
        if input[new_x][new_y] == letter:
            num_corners -=1
            _, per = find_region(new_x, new_y, input, letter, nodes)
            perimeter += per
    perimeter += num_corners
    return nodes, perimeter

def find_region_part_two(x, y, input, letter, nodes, all_sides):
    nodes.add((x, y))
    sides = 0
    num_corners = 4

    # i want to keep a set of the sides, where each side is a plane (2,0) or(2,0)
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
        
            continue
        if input[new_x][new_y] != letter:
            all_sides.add((direction[0] * new_x, direction[1] * new_y))
    
    # diff = corner_directions - prev_corner_directions

    # diff = diff - set(existing)
    # print(corner_directions, prev_corner_directions)
    # print(x,y, input[x][y], diff)
    # sides += len(diff)

    # all_sides[(x,y)] = diff
    
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
            continue
        if (new_x, new_y) in nodes:
            num_corners -= 1
            continue
        if input[new_x][new_y] == letter:
            num_corners -= 1
            find_region_part_two(
                new_x, new_y, input, letter, nodes, all_sides
            )
            
            
    len(all_sides)
    return nodes, all_sides
        

def main() -> None:
    input = parse_file("input.txt")

    rows = len(input)
    cols = len(input[0])
    plants_in_plots = set()
    plants_in_plots_2 = set()
    total = 0
    total2 = 0 
    for row in range(rows):
        for col in range(cols):
            if (row, col) in plants_in_plots:
                continue
            letter = input[row][col]
            nodes, perimeter = find_region(row, col, input, letter, set())
            total += len(nodes) * perimeter
            for node in nodes:
                plants_in_plots.add(node)
            
            nodes, sides = find_region_part_two(row, col, input, letter, set(), set())
            total2 += len(sides) * len(nodes)
            for node in nodes:
                plants_in_plots_2.add(node)
            print(input[row][col], sides)

            # graph search 
    print(total)
    print(total2)

if __name__ == "__main__":
    main()
