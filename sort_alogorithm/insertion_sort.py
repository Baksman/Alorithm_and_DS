

def insertion_sort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
# j >= 0 and
        while key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
    customList[j+1] = key
 
    return customList
 

customList = [10, 59, 588, 440, 283]
insertion_sort(customList)
