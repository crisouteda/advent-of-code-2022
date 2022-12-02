points = {'X': 1, 'Y': 2, 'Z': 3}
result = {'A':
          {
              'X': "=",
              'Y': '+',
              'Z': '-'
          },
          'B':
          {
              'X': "-",
              'Y': '=',
              'Z': '+'
          },
          'C':
          {
              'X': "+",
              'Y': '-',
              'Z': '='
          }
          }
resultPoints = {'+': 6, '=': 3, '-': 0}


def findTotalPoints():
    totalPoints = 0
    with open('./input.txt') as f:
        lines = f.readlines()
    for line in lines:
        totalPoints += findResultPerRound(line[0], line[2])
    return totalPoints


def findResultPerRound(o, m):
    roundPoints = points[m]
    roundPoints += resultPoints[result[o][m]]
    return roundPoints


result = findTotalPoints()
print(result)
