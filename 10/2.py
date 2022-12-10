def findTotal():
    with open('./input.txt') as f:
        lines = f.readlines()
    x = 1
    cicles = 0
    row = []
    for i in range(len(lines)):
        if lines[i][:4] == 'noop':
            cicles += 1
            row = check_if_sume(cicles, x, row)
        elif lines[i][:4] == 'addx':
            cicles += 1
            row = check_if_sume(cicles, x, row)
            cicles += 1
            row = check_if_sume(cicles, x, row)
            line = lines[i][4:].replace(' ', '')
            x += int(line)
    print_row = ''.join(str(e) for e in row)
    print(print_row)


def check_if_sume(cicles, x, row):
    if len(row) == 40:
        print_row = ''.join(str(e) for e in row)
        print(print_row)
        char = '#' if (x == 0 or x-1 == 0 or x+1 == 0) else '.'
        return [char]
    else:
        index = cicles % 40 - 1
        char = '#' if (x == index or x-1 == index or x+1 == index) else '.'
        row.append(char)
        return row


findTotal()

# ELPLZGZL

# NOTE: There is an error calculating the last element of each list but this code was enough to get the right answer
