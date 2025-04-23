

import itertools
import re


def parse_file(file_name):
    with open(file_name) as f:
        return [ line.strip().split(":") for line in f]
    
# 1611660863222
def main() -> None:
    input = parse_file("input.txt")
    operators = ["*", "+", "||"]

    total_result = 0 
    for row in input:
        total = int(row[0])
        numbers =  [ int(x) for x in row[1][1:].split(" ")]
        print("Total: ", total, "Numbers: ", numbers)
        
        product =  eval('*'.join(map(str, numbers)))
        if product == total:
            print("Found: ", numbers)
            total_result += total
            continue

        if sum(numbers) == total:
            print("Found: ", numbers)
            total_result += total
            continue
        
        combinations = list(itertools.product(operators, repeat=len(numbers)-1))
        for combination in combinations:
            expression = ""
    
            for i in range(len(numbers)-1):
                expression += str(numbers[i]) + combination[i]
        
            expression += str(numbers[-1])
            evaluated_value = evaluate_left_to_right(expression)
            if evaluated_value == total:
                print("Found: ", expression)
                total_result += total
                break
    print(total_result)


def evaluate_left_to_right(expression: str) -> int:
    tokens = re.findall(r"\d+|\+|\*|\|\|", expression)
    
    total = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if tokens[i] == "+":
            total += int(tokens[i+1])
        elif tokens[i] == "*":
            total *= int(tokens[i+1])
        elif tokens[i] == "||":
            total = int(str(total) + (tokens[i+1]))
    return total


if __name__ == "__main__":
    main()