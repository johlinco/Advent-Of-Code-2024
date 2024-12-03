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


def part1(rows):
    safe_reports = 0
    for line in rows.readlines():
        report = line.split(" ")
        if (safe_or_unsafe(report)):
            safe_reports += 1

    return safe_reports


print(part1(example_rows))
print(part1(input_rows))
example_rows.close()
input_rows.close()
