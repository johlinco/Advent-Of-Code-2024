import re

example_rows = open("example.txt")
input_rows = open("input.txt")

example_input = example_rows.read().strip()
input_input = input_rows.read().strip()


def part1(puzzle_input):
    total = 0
    print(re.findall(r"mul\((\d+),(\d+)\)", puzzle_input))
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", puzzle_input):
        total += int(a) * int(b)

    return total


print(part1(example_input))
# print(part1(input_input))
