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
    if firstBeg <= secondBeg:
        if firstBeg == secondBeg:
            return 1
        if (firstEnd >= secondBeg):
            return 1
        if (firstEnd < secondBeg):
            return 0
    if secondBeg <= firstBeg:
        if secondBeg == firstBeg:
            return 1
        if (secondEnd >= firstBeg):
            return 1
        if (secondEnd < firstBeg):
            return 0
    return 0


print(findTotalPoints())
