vectors = {
    'U': [0, 1],
    'D': [0, -1],
    'R': [1, 0],
    'L': [-1, 0],
}


def get_next_move_coord(diff):
    [x, y] = diff
    if ((x == 0 and y == 0) or (abs(x) == 1 and y == 0) or (x == 0 and abs(y) == 1) or (abs(x) == 1 and abs(y) == 1)):
        return [0, 0]
    elif (x == 0 or y == 0):
        if x == 0 and y > 1:
            return [0, 1]
        elif y == 0 and x > 1:
            return [1, 0]
        elif x == 0 and y < -1:
            return [0, -1]
        elif y == 0 and x < -1:
            return [-1, 0]
        else:
            print("error aqui", diff)
    elif (abs(x) > 1 or abs(y) > 1):
        if x > 1:
            return [1, y]
        elif x < -1:
            return [-1, y]
        elif y > 1:
            return [x, 1]
        elif y < -1:
            return [x, -1]
        else:
            print("error aqui", diff)


def findTotal():
    with open('./input.txt') as f:
        lines = f.readlines()
    head_last_position = [0, 0]
    tail_last_position = [0, 0]
    tail_positions = set()

    for line in lines:
        [direction_code, number] = [line[0], int(line[2:].replace(' ', ''))]
        direction = vectors[direction_code]
        while number > 0:
            # move head
            head_last_position = [sum(pair)
                                  for pair in zip(direction, head_last_position)]
            # check difference between head and tail
            difference_in_position = [sum([pair[0], -pair[1]])
                                      for pair in zip(head_last_position, tail_last_position)]
            # calculate new tail position
            next_move_coord = get_next_move_coord(difference_in_position)
            tail_last_position = [sum(pair)
                                  for pair in zip(tail_last_position, next_move_coord)]
            tail_positions.add(str(tail_last_position))
            number -= 1
    print('total:', len(tail_positions))


findTotal()
