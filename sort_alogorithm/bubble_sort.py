# Types of sirting algorithm
# 1.space used
# a.In place e.g bubble sort
# b.Out of place e.g merge sort
# 2.Stability
# a.Stable .. doesnt change sequence of identical item
# b.Unstable .. changes sequence of identical item e.q quick sort


def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1-i):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]

    print(customList)


customList = [10, 59, 588, 440, 283, 99, 33, 3839]
# bubbleSort(customList)
# 1,2,3,4,5,6,7,8,9


def bbSort(cList):
    for i in range(len(customList)):
        i += 1
        for i in range(len(cList)-1):
            if customList[i] > customList[i+1]:
                customList[i], customList[i+1] = customList[i+1], customList[i]
    return customList


print(bbSort(customList))
