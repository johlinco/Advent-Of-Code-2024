example_lines = open('example.txt')
input_lines = open('input.txt')


def part1(input, cols, rows):

    quadrants = {
        'up': {
            'left': 0,
            'right': 0,
        },
        'down': {
            'left': 0,
            'right': 0,
        },
    }

    def guard_mover(x_pos, y_pos, x_move, y_move, x_max, y_max, moves):
        while moves > 0:
            x_pos = x_pos + x_move
            if x_pos >= x_max:
                x_pos = x_pos - x_max
            if x_pos < 0:
                x_pos = x_pos + x_max

            y_pos = y_pos + y_move
            if y_pos >= y_max:
                y_pos = y_pos - y_max
            if y_pos < 0:
                y_pos = y_pos + y_max

            moves -= 1

        y_side = None
        x_side = None
        if x_max // 2 > x_pos:
            x_side = "left"
        elif x_max // 2 < x_pos:
            x_side = "right"

        if y_max // 2 > y_pos:
            y_side = "up"
        elif y_max // 2 < y_pos:
            y_side = "down"

        if y_side and x_side:
            quadrants[y_side][x_side] += 1

    for line in input:

        [pos, vel] = line.split()
        pos = pos.split('=')[1].split(',')
        vel = vel.split('=')[1].split(',')
        x_pos = int(pos[0])
        y_pos = int(pos[1])
        x_move = int(vel[0])
        y_move = int(vel[1])

        guard_mover(x_pos, y_pos, x_move, y_move, cols, rows, 100)

    print(quadrants['up']['left'], quadrants['up']['right'],
          quadrants['down']['left'], quadrants['down']['right'])

    print(quadrants['up']['left'] * quadrants['up']['right'] *
          quadrants['down']['left'] * quadrants['down']['right'])


part1(example_lines, 11, 7)
part1(input_lines, 101, 103)
