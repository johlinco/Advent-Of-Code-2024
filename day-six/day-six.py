import copy

example_rows = open("example.txt")
input_rows = open("input.txt")

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

guards = {
    '<': 'left',
    '>': 'right',
    '^': 'up',
    'v': 'down',
}

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
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] in guards:
                return [i, j, guards[matrix[i][j]]]


def part1(matrix):

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


def part2(matrix):
    loop_count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(i, j)
            # if matrix[i][j] == '#' or matrix[i][j] in guards:
            #     continue
            # else:
            new_matrix = copy.deepcopy(matrix)
            new_matrix[i][j] = '#'
            # for row in new_matrix:
            #     print(row)

            visited = {}

            [y, x, dir] = find_guard(matrix)

            visited = {f"{y},{x},{dir}"}

            while (x > 0 and x < len(new_matrix[0])-1 and y > 0 and y < len(new_matrix)-1):
                # print(x, y)
                # if next move would run into object, change dir
                if new_matrix[y + guard_move[dir]['y_move']][x + guard_move[dir]['x_move']] == '#':
                    dir = guard_move[dir]['next']
                # if next move has already been done and is found in the set, you found a loop
                    # add one to loop count
                    # break out of while loop

                if (f"{y + guard_move[dir]['y_move']},{x + guard_move[dir]['x_move']},{dir}" in visited):
                    loop_count += 1
                    print('ding')
                    break
                # if position and direction aren't in visited set, add them to visited set
                else:
                    visited.add(
                        f"{y + guard_move[dir]['y_move']},{x + guard_move[dir]['x_move']},{dir}")
                y = y + guard_move[dir]['y_move']
                x = x + guard_move[dir]['x_move']
    return loop_count


# print(part2(example_matrix))
# print(part2(input_matrix))
print(find_guard(input_matrix))
