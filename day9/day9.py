from typing import List


def parse_file(str: str) -> List[str]:
    with open(str) as f:
        return [int(x) for x in list(f.readline().strip())]


def parse_input(
    input: List[int],
) -> tuple[dict[int, tuple[int, int]], dict[int, tuple[int, int]]]:
    freespace: List[tuple[int, int]] = []
    files: dict[int, tuple[int, int]] = {}

    expanded_idx = 0
    for i, r in enumerate(input):
        if i % 2 == 0:
            files[i // 2] = (expanded_idx, int(r))
        else:
            freespace.append((expanded_idx, int(r)))
        expanded_idx += int(r)
    return files, freespace


def main() -> None:
    input = parse_file("input.txt")

    expanded = []
    for i, r in enumerate(input):
        if i % 2 == 0:
            for k in range(int(r)):
                expanded.append(f"{i // 2}")
        else:
            for k in range(int(r)):
                expanded.append(".")

    free_space_idx = 0
    end_ptr = len(expanded) - 1

    while free_space_idx < end_ptr:
        while expanded[free_space_idx] != ".":
            free_space_idx += 1
        while expanded[end_ptr] == ".":
            end_ptr -= 1
        # move from back to front
        expanded[free_space_idx] = expanded[end_ptr]
        expanded[end_ptr] = "."
        end_ptr -= 1
        free_space_idx += 1

    # remove all the dots
    expanded = [e for e in expanded if e != "."]
    print("Part1")
    print(sum([int(i) * int(k) for i, k in enumerate(expanded)]))

    print("Part2")

    files, free_space = parse_input(input)

    for file_id in reversed(files):
        file_idx, length = files[file_id]
        # go through free space
        for i, (idx, space) in enumerate(free_space):
            if idx > file_idx:
                continue
            if length > space:
                continue
            if length <= space:
                # update the file location
                files[file_id] = (idx, length)
                # update the free space
                free_space[i] = (idx + length, space - length)
                break

    total = 0
    for file_id, (idx, length) in files.items():
        for j in range(length):
            total += file_id * (idx + j)
    print(total)


if __name__ == "__main__":
    main()
