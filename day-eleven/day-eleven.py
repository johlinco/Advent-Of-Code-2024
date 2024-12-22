from functools import cache

example_array = open("example.txt").read().split()
input_array = open("input.txt").read().split()

example_stones = [int(x) for x in example_array]
input_stones = [int(x) for x in input_array]


@cache
def stone_counter(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return stone_counter(1, steps - 1)
    string = str(stone)
    length = len(string)
    midpoint = length // 2
    if length % 2 == 0:
        return stone_counter(int(string[:midpoint]), steps - 1) + stone_counter(int(string[midpoint:]), steps - 1)
    return stone_counter(stone * 2024, steps - 1)


print(input_stones)
print(sum(stone_counter(stone, 75) for stone in input_stones))
