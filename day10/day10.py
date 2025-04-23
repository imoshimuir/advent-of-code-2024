def parse_file(str: str) -> None:
    with open(str) as f:
        return [[int(x) for x in line.strip()] for line in f]

def main():
    grid = parse_file("input.txt")

    total = 0
    total_score = 0
    for x, row in enumerate(grid):
        for y, num in enumerate(row):
            if num == 0:
                total_trail, peak_locations = follow_trail(x, y, 0, grid, set())
                total_score += len(peak_locations)
                total += total_trail
                continue
    print(total_score)
    print(total)

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def follow_trail(x,y, curr_num, input, peak_locations) -> int:
    total = 0
    if curr_num == 9:
        print("Reached end")
        peak_locations.add((x,y))
        return 1, peak_locations

    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
            # out of bounds
            continue

        if input[new_x][new_y] == curr_num + 1:
            print("Follow trail", curr_num + 1)
            sum, peak_locations = follow_trail(new_x, new_y, curr_num + 1, input, peak_locations)
            total += sum
    return total, peak_locations

if __name__ == "__main__":
    main()
