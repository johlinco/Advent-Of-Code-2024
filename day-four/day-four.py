example_rows = open("example.txt")
input_rows = open("input.txt")

dirs = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 1], [-1, 0], [-1, -1]]


def matrix_builder(input):
    matrix = []
    for line in input:
        items = []
        for char in line:
            if char != '\n':
                items.append(char)
        matrix.append(items)
    return matrix


def within_bounds(matrix, pos, dir, dist):
    return 0 <= pos[0] + dist * dir[0] < len(matrix) and 0 <= pos[1] + dist * dir[1] < len(matrix[0])


def xmas_check(matrix, pos, dir):
    x = pos[0]
    y = pos[1]
    x_move = dir[0]
    y_move = dir[1]
    if not within_bounds(matrix, pos, dir, 1) or not within_bounds(matrix, pos, dir, 2) or not within_bounds(matrix, pos, dir, 3):
        return False
    if matrix[x + x_move][y + y_move] != "M":
        return False
    if matrix[x + 2 * x_move][y + 2 * y_move] != "A":
        return False
    if matrix[x + 3 * x_move][y + 3 * y_move] != "S":
        return False
    return True


def xmas_count(matrix):
    xmas_counter = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            for k in range(0, len(dirs)):
                if matrix[i][j] == 'X':
                    if xmas_check(matrix, [i, j], dirs[k]):
                        xmas_counter += 1
    return xmas_counter


def descend_mas(matrix, x, y):
    set = {'M', 'S'}
    set.discard(matrix[x-1][y-1])
    set.discard(matrix[x+1][y+1])
    return len(set) == 0


def ascend_mas(matrix, x, y):
    set = {'M', 'S'}
    set.discard(matrix[x-1][y+1])
    set.discard(matrix[x+1][y-1])
    return len(set) == 0


def part2(input):
    matrix = matrix_builder(input)
    xmas_count = 0

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == 'A':
                xmas_count += (ascend_mas(matrix, i, j)
                               and descend_mas(matrix, i, j))

    return xmas_count


def part1(input):
    matrix = matrix_builder(input)
    return xmas_count(matrix)


# print(part1(example_rows))
# print(part1(input_rows))

print(part2(example_rows))
print(part2(input_rows))

example_rows.close()
input_rows.close()
