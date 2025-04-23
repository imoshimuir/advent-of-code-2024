from typing import List
from collections import deque


def parse_file(str: str) -> List[int]:
    with open(str) as f:
        return [int(x) for x in list(f.readline().split(" "))]

def get_next_numbers(num: int) -> List[int]:
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        first = str(num)[: len(str(num)) // 2]
        second = str(num)[len(str(num)) // 2 :]
        return [int(first), int(second)]
    else:
        return [num * 2024]


cache = {}
def main() -> None:
    input = deque(parse_file("input.txt"))

    for j in range(0, 25):
        length = len(input)
        for _ in range(length):
            current = input.popleft()
            if current == 0:
                input.append(1)
            elif len(str(current)) % 2 == 0:
                first = str(current)[: len(str(current)) // 2]
                second = str(current)[len(str(current)) // 2 :]
                input.append(int(first))
                input.append(int(second))
            else:
                input.append(current * 2024)
        # print(j, len(input))
        # print(input)
    print(len(input))


    sum = iterate_through_nums(parse_file("input.txt"), curr=0)
    print(sum)

         
def iterate_through_nums(nums: List[int], curr) -> int:
    sum = 0

    if curr == 75:
        return len(nums)
    curr += 1
    for num in nums:
        next_nums = get_next_numbers(num)
        if (tuple(next_nums), curr) in cache:
            sum += cache[(tuple(next_nums), curr)]
        else:
            count = iterate_through_nums(next_nums, curr)
            cache[(tuple(next_nums), curr)] = count
            sum += count
    

    return sum

if __name__ == "__main__":
    main()