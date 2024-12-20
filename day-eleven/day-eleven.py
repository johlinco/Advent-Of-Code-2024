example_array = open("example.txt").read().split()
input_array = open("input.txt").read().split()


def stone_parser(array):
    result = []

    for stone in array:
        stone_int = int(stone)
        if stone_int == 0:
            result.append("1")
        elif len(stone) % 2 == 0:
            midpoint = len(stone) // 2
            result.append(stone[:midpoint])
            if int(stone[midpoint:]) == 0:
                result.append("0")
            else:
                back_half = stone[midpoint:]
                while back_half[0] == "0":
                    back_half = back_half[1:]
                result.append(back_half)
        else:
            result.append(str(stone_int * 2024))

    return result


def stone_looper(loops, array):

    for i in range(0, loops):
        array = stone_parser(array)

    return len(array)


print(stone_looper(25, example_array))
print(stone_looper(25, input_array))
