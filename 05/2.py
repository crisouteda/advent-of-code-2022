def findTotalPoints():
    boardTest = [["Z", "N"], ["M", "C", "D"], ["P"]]
    boardInput = [['G', 'D', 'V', 'Z', 'J', 'S', "B"],
                  ['Z', 'S', 'M', 'G', 'V', 'P'],
                  ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
                  ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
                  ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
                  ['R', 'G', 'C', 'D'],
                  ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
                  ['P', 'F', 'V'],
                  ['D', 'R', 'S', 'T', 'J'],
                  ]
    board = boardInput
    with open('./input.txt') as f:
        lines = f.readlines()
    for line in lines[10:]:
        [amount, from_col, to_row] = findNumbersPerRow(line)

        moved = board[from_col][-amount:]
        board[from_col] = board[from_col][:-amount]
        board[to_row] += moved

    final_string = ""

    for item in board:
        final_string += item[-1]
    print(final_string)


def findNumbersPerRow(line):
    numbers = []
    items = line.replace("\n", "").split(' ')
    for item in items:
        if item.isnumeric():
            numbers.append(int(item))
    # -1 to adjust from number of column to index
    return [numbers[0], numbers[1]-1, numbers[2]-1]


findTotalPoints()
