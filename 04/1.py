def findTotalPoints():
    totalMatch = 0
    with open('./input.txt') as f:
        lines = f.readlines()
    for line in lines:
        [first, second] = line.split(",")
        [firstBeg, firstEnd] = first.split("-")
        [secondBeg, secondEnd] = second.split("-")
        totalMatch += checkIfCointains(int(firstBeg),
                                       int(firstEnd), int(secondBeg), int(secondEnd))
    return totalMatch


def checkIfCointains(firstBeg, firstEnd, secondBeg, secondEnd):
    if (firstBeg <= secondBeg):
        if (firstEnd >= secondEnd):
            return 1
    if (secondBeg <= firstBeg):
        if (secondEnd >= firstEnd):
            return 1
    return 0


print(findTotalPoints())
