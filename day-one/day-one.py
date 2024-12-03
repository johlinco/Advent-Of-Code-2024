example_rows = open("example.txt")
input_rows = open("input.txt")


def read_input(rows):
    left_col, right_col = [], []
    for line in rows.readlines():
        nums = line.split(" ")
        right_col.append(int(nums[0]))
        left_col.append(int(nums[3]))

    left_col.sort()
    right_col.sort()

    return left_col, right_col


def part1(rows):
    left_col, right_col = read_input(rows)
    diff_sum = 0

    for i in range(0, len(right_col)):
        diff_sum += (abs(right_col[i] - left_col[i]))

    return diff_sum


def part2(rows):
    left_col, right_col = read_input(rows)
    similarity_score = 0
    freq_table = {}

    for num in right_col:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1

    for num in left_col:
        if num in freq_table:
            similarity_score += num * freq_table[num]

    return similarity_score


# print(part1(example_rows))
# print(part1(input_rows))
print(part2(example_rows))
print(part2(input_rows))
example_rows.close()
input_rows.close()
