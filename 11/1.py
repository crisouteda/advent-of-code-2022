monkeys_input = [
    # 0
    {
        'starting': [93, 54, 69, 66, 71],
        'calc': lambda x: x*3,
        'operation': lambda x: 7 if x % 7 == 0 else 1
    },
    # 1
    {
        'starting': [89, 51, 80, 66],
        'calc': lambda x: x*17,
        'operation': lambda x: 5 if x % 19 == 0 else 7
    },
    # 2
    {
        'starting': [90, 92, 63, 91, 96, 63, 64],
        'calc': lambda x: x+1,
        'operation': lambda x: 4 if x % 13 == 0 else 3
    },
    # 3
    {
        'starting': [65, 77],
        'calc': lambda x: x+2,
        'operation': lambda x: 4 if x % 3 == 0 else 6
    },
    # 4
    {
        'starting': [76, 68, 94],
        'calc': lambda x: x*x,
        'operation': lambda x: 0 if x % 2 == 0 else 6
    },
    # 5
    {
        'starting': [86, 65, 66, 97, 73, 83],
        'calc': lambda x: x+8,
        'operation': lambda x: 2 if x % 11 == 0 else 3
    },
    # 6
    {
        'starting': [78],
        'calc': lambda x: x+6,
        'operation': lambda x: 0 if x % 17 == 0 else 1
    },
    # 7
    {
        'starting': [89, 57, 59, 61, 87, 55, 55, 88],
        'calc': lambda x: x+7,
        'operation': lambda x: 2 if x % 5 == 0 else 5
    },
]

monkeys_test = [
    # 0
    {
        'starting': [79, 98],
        'calc': lambda x: x*19,
        'operation': lambda x: 2 if x % 23 == 0 else 3
    },
    # 1
    {
        'starting': [54, 65, 75, 74],
        'calc': lambda x: x+6,
        'operation': lambda x: 2 if x % 19 == 0 else 0
    },
    # 2
    {
        'starting': [79, 60, 97],
        'calc': lambda x: x*x,
        'operation': lambda x: 1 if x % 13 == 0 else 3
    },
    # 3
    {
        'starting': [74],
        'calc': lambda x: x+3,
        'operation': lambda x: 0 if x % 17 == 0 else 1
    },
]

monkeys = monkeys_input

counts = [0] * len(monkeys)

for i in range(20):
    for monkey in range(len(monkeys)):
        for item in monkeys[monkey]['starting']:
            item = monkeys[monkey]['calc'](item)
            item //= 3
            next_monkey = monkeys[monkey]['operation'](item)
            monkeys[next_monkey]['starting'].append(item)
        counts[monkey] += len(monkeys[monkey]['starting'])
        monkeys[monkey]['starting'] = []

counts.sort()
print(counts[-1] * counts[-2])
