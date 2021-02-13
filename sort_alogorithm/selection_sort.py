

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


customList = [10, 59, 588, 440, 283]
selectionSort(customList)


# 1,2,3,4,5,,7,8,9,
