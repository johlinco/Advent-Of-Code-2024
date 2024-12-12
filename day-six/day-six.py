example_rows = open("example.txt")
input_rows = open("input.txt")

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def matrix_builder(input):
    matrix = []
    for line in input:
        items = []
        for char in line:
            if char != '\n':
                items.append(char)
        matrix.append(items)
    return matrix


example_matrix = matrix_builder(example_rows)
input_matrix = matrix_builder(input_rows)


def find_guard(matrix):
    # print(matrix)
    guards = {
        '<': 'left',
        '>': 'right',
        '^': 'up',
        'v': 'down',
    }
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] in guards:
                return [i, j, guards[matrix[i][j]]]


def part1(matrix):
    guard_move = {
        'up': {
            'x_move': 0,
            'y_move': -1,
            'next': 'right',
        },
        'right': {
            'x_move': 1,
            'y_move': 0,
            'next': 'down',
        },
        'down': {
            'x_move': 0,
            'y_move': 1,
            'next': 'left',
        },
        'left': {
            'x_move': -1,
            'y_move': 0,
            'next': 'up',
        }
    }

    visited = {}

    [y, x, dir] = find_guard(matrix)

    visited = {f"{y},{x}"}

    while (x > 0 and x < len(matrix[0])-1 and y > 0 and y < len(matrix)-1):
        if matrix[y + guard_move[dir]['y_move']][x + guard_move[dir]['x_move']] == '#':
            dir = guard_move[dir]['next']

        visited.add(
            f"{y + guard_move[dir]['y_move']},{x + guard_move[dir]['x_move']}")

        y = y + guard_move[dir]['y_move']
        x = x + guard_move[dir]['x_move']

    return len(visited)


print(part1(example_matrix))
print(part1(input_matrix))

# print(part1(example_rows))
# print(part1(input_rows))
# print(part2(example_rows))
# print(part2(input_rows))
