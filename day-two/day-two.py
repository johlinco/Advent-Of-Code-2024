example_rows = open("example.txt")
input_rows = open("input.txt")


def safe_or_unsafe(arr):
    if int(arr[1]) > int(arr[0]):
        dir = "up"
    else:
        dir = "not up"

    for i in range(1, len(arr)):
        first = int(arr[i-1])
        second = int(arr[i])
        if second == first or abs(second - first) > 3:
            return False
        if dir == "up" and second < first:
            return False
        if dir != "up" and second > first:
            return False

    return True


def safe_or_unsafe_damper(arr):
    if safe_or_unsafe(arr):
        return True

    for i in range(0, len(arr)):
        new_arr = []
        for j in range(0, len(arr)):
            if j != i:
                new_arr.append(arr[j])
        if safe_or_unsafe(new_arr):
            return True
    return False


def part1(rows):
    safe_reports = 0
    for line in rows.readlines():
        report = line.split(" ")
        if (safe_or_unsafe(report)):
            safe_reports += 1

    return safe_reports


def part2(rows):
    safe_reports = 0
    for line in rows.readlines():
        report = line.split(" ")
        if (safe_or_unsafe_damper(report)):
            safe_reports += 1

    return safe_reports


# print(part1(example_rows))
# print(part1(input_rows))
print(part2(example_rows))
print(part2(input_rows))

example_rows.close()
input_rows.close()
