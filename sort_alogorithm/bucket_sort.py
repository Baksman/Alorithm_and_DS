import math


def bucketSort(customList):
    number_of_bucket = round(math.sqrt(len(customList)))
    max_value = max(customList)

    arr = []
    for i in range(number_of_bucket):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*number_of_bucket/max_value)
        arr[index_b-1].append(j)

    k = 0

    for i in range(number_of_bucket):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


customList = [10, 59, 588, 440, 283]
print(bucketSort(customList))
