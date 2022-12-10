def findTotalTrees():
    with open('./input.txt') as f:
        input = f.readlines()
        n_lines = len(input)
        len_row = len(input[0])-1
        forest = []
        turned_forest = [[0] * len_row for _ in range(n_lines)]
        for line in input:
            forest.append([int(x) for x in line[:-1]])
        for i in range(len(turned_forest)):
            for j in range(len(turned_forest[0])):
                turned_forest[i][j] = forest[j][i]

        visible = 0

        for i in range(n_lines):
            for j in range(len_row):
                tree = forest[i][j]
                if i == 0 or j == 0 or i == n_lines-1 or j == len_row-1:
                    visible += 1
                    continue
                if tree > max(forest[i][:j]) or tree > max(forest[i][j+1:]) or tree > max(turned_forest[j][:i]) or tree > max(turned_forest[j][i+1:]):
                    visible += 1
                    continue
        print('visible', visible)


findTotalTrees()

# 1812 is right
