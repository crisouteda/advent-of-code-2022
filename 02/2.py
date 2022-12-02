points = {'B': 2, 'A': 1, 'C': 3}
resultPoints = {'Z': 6, 'Y': 3, 'X': 0}
result = {'A':
          {
              'X': "C",
              'Y': 'A',
              'Z': 'B'
          },
          'B':
          {
              'X': "A",
              'Y': 'B',
              'Z': 'C'
          },
          'C':
          {
              'X': "B",
              'Y': 'C',
              'Z': 'A'
          }
          }


def findTotalPoints():
    totalPoints = 0
    with open('./input.txt') as f:
        lines = f.readlines()
        for line in lines:
            totalPoints += findResultPerRound(line[0], line[2])
        return totalPoints


def findResultPerRound(o, r):
    roundPoints = resultPoints[r]
    roundPoints += points[result[o][r]]
    return roundPoints


result = findTotalPoints()
print(result)
