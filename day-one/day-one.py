example_rows = open("example.txt", "r")
input_rows = open("input.txt", "r")


def part1(rows):
    left_col, right_col = [], []
    for line in rows.readlines():
        nums = line.split(" ")
        right_col.append(int(nums[0]))
        left_col.append(int(nums[3]))

    left_col.sort()
    right_col.sort()
    diff_sum = 0

    for i in range(0, len(right_col)):
        diff_sum += (abs(right_col[i] - left_col[i]))

    return diff_sum


print(part1(example_rows))
print(part1(input_rows))

example_rows.close()
input_rows.close()
