print("started")


def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1-i):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
        

    print(customList)


customList = [10, 59, 588, 440, 283]
bubbleSort(customList)
