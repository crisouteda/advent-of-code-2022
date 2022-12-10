vectors = {
    'U': [0, 1],
    'D': [0, -1],
    'R': [1, 0],
    'L': [-1, 0],
}


def print_tail_positions(tail_positions):
    board = [['.'] * 25 for _ in range(15)]
    for n in tail_positions:
        n = n.replace('[', '').replace(']', '')
        n = n.split(',')
        [x, y] = n
        board[int(y)][int(x)] = '#'
    for b in board:
        a = ''.join(e for e in b)
        print(a)


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
            print("error here", diff)
    elif (abs(x) > 1 and abs(y) > 1):
        if x > 1 and y > 1:
            return [1, 1]
        elif x > 1 and y < -1:
            return [1, -1]
        elif x < -1 and y > 1:
            return [-1, 1]
        elif x < -1 and y < -1:
            return [-1, -1]
        else:
            print("error here", diff)
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
            print("error here", diff)


def findTotal():
    with open('./input.txt') as f:
        lines = f.readlines()
    last_position = [[11, 5] for i in range(10)]
    tail_positions = set()

    for line in lines:
        [direction_code, number] = [line[0], int(line[2:].replace(' ', ''))]
        direction = vectors[direction_code]
        for _ in range(number):
            # move head
            last_position[0] = [sum(pair)
                                for pair in zip(direction, last_position[0])]
            for i in range(1, 10):
                # check difference between head and tail
                difference_in_position = [sum([pair[0], -pair[1]])
                                          for pair in zip(last_position[i-1], last_position[i])]
                # calculate new tail position
                next_move_coord = get_next_move_coord(difference_in_position)
                last_position[i] = [sum(pair)
                                    for pair in zip(last_position[i], next_move_coord)]
            tail_positions.add(str(last_position[-1]))
    print('total:', len(tail_positions))
    # print_tail_positions(tail_positions)


findTotal()
#result: 2443
