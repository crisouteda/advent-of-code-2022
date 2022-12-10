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
        highest_scenic_score = 0

        for i in range(n_lines):
            for j in range(len_row):
                tree = forest[i][j]
                scenic_score = 0
                if i == 0 or j == 0 or i == n_lines-1 or j == len_row-1:
                    visible += 1
                    continue
                scenic_score = get_position_first_high_tree(
                    forest[i][:j][::-1], tree)
                scenic_score *= get_position_first_high_tree(
                    forest[i][j+1:], tree)
                scenic_score *= get_position_first_high_tree(
                    turned_forest[j][:i][::-1], tree)
                scenic_score *= get_position_first_high_tree(
                    turned_forest[j][i+1:], tree)
                highest_scenic_score = max(highest_scenic_score, scenic_score)

        print('highers scenic score', highest_scenic_score)


def get_position_first_high_tree(list, height):
    for i in range(len(list)):
        if list[i] >= height:
            return i+1
    return len(list)


findTotalTrees()

# highers scenic score 315495
