def findHighestSume():
    sumes = [0]
    counter = 0
    with open('./input.txt') as f:
        lines = f.readlines()
        for i in lines:
            if i[:-1].isnumeric():
                sumes[counter] += int(i[:-1])
            else:
                counter += 1
                sumes.append(0)
        return max(sumes)


result = findHighestSume()
print(result)
