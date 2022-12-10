def findTotal():
    with open('./input.txt') as f:
        lines = f.readlines()
    x = 1
    total = 0
    cicles = 0

    for i in range(len(lines)):
        if lines[i][:4] == 'noop':
            cicles += 1
            total += check_if_sume(cicles, x, i)
        elif lines[i][:4] == 'addx':
            cicles += 1
            total += check_if_sume(cicles, x, i)
            cicles += 1
            total += check_if_sume(cicles, x, i)
            line = lines[i][4:].replace(' ', '')
            x += int(line)
        if cicles >= 220:
            break
    print("total ", total)


def check_if_sume(cicles, x, i):
    if ((cicles - 20) % 40 == 0):
        print("cicle, multiplicacion", cicles, cicles*x, x, i)
        return cicles * x
    else:
        return 0


findTotal()
