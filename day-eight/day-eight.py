example_rows = open("example.txt")
input_rows = open("input.txt")


def matrix_builder(input):
    matrix = []
    for line in input:
        items = []
        for char in line:
            if char != '\n':
                items.append(char)
        matrix.append(items)
    return matrix


def antenna_placer(x1, y1, x2, y2, max_row, max_col, antenna_set):
    min_X = min(x1, x2)
    max_X = max(x1, x2)
    min_Y = min(y1, y2)
    max_Y = max(y1, y2)
    diff_X = max_X - min_X
    diff_Y = max_Y - min_Y

    if x1 == max_X:
        x1 = x1 + diff_X
        x2 = x2 - diff_X
    else:
        x1 = x1 - diff_X
        x2 = x2 + diff_X

    if y1 == max_Y:
        y1 = y1 + diff_Y
        y2 = y2 - diff_Y
    else:
        y1 = y1 - diff_Y
        y2 = y2 + diff_Y

    if 0 <= x1 < max_col and 0 <= y1 < max_row:
        antenna_set.add(f"{x1},{y1}")

    if 0 <= x2 < max_col and 0 <= y2 < max_row:
        antenna_set.add(f"{x2},{y2}")


def resonant_antenna_placer(x1, y1, x2, y2, max_row, max_col, resonant_antenna_set):
    resonant_antenna_set.add(f"{x1},{y1}")

    x_diff = x2 - x1
    y_diff = y2 - y1

    new_x = x1 + x_diff
    new_y = y1 + y_diff

    while 0 <= new_x < max_col and 0 <= new_y < max_row:
        resonant_antenna_set.add(f"{new_x},{new_y}")
        new_x = new_x + x_diff
        new_y = new_y + y_diff

    new_x = x1 - x_diff
    new_y = y1 - y_diff

    while 0 <= new_x < max_col and 0 <= new_y < max_row:
        resonant_antenna_set.add(f"{new_x},{new_y}")
        new_x = new_x - x_diff
        new_y = new_y - y_diff


def antennas(input):
    input_matrix = matrix_builder(input)
    antenna_set = set()
    resonant_antenna_set = set()

    position_dictionary = {}

    for i in range(0, len(input_matrix)):
        for j in range(0, len(input_matrix[0])):
            if input_matrix[i][j] != ".":
                if input_matrix[i][j] not in position_dictionary:
                    position_dictionary[input_matrix[i][j]] = [[i, j]]
                else:
                    position_dictionary[input_matrix[i][j]].append([i, j])

    for value in position_dictionary.values():
        for k in range(0, len(value)):
            for l in range(k+1, len(value)):
                x1 = value[k][1]
                y1 = value[k][0]
                x2 = value[l][1]
                y2 = value[l][0]
                antenna_placer(x1, y1, x2, y2, len(input_matrix),
                               len(input_matrix[0]), antenna_set)
                resonant_antenna_placer(x1, y1, x2, y2, len(input_matrix),
                                        len(input_matrix[0]), resonant_antenna_set)

    return [len(antenna_set), len(resonant_antenna_set)]


print(antennas(example_rows))
print(antennas(input_rows))
