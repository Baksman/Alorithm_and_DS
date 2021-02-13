import math


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


# customList = [10, 59, 588, 440, 283]
# insertion_sort(customList)


def bucketSort(customList):
    number_of_bucket = round(math.sqrt(len(customList)))
    max_value = max(customList)
    # a list of alist
    arr = []
    for i in range(number_of_bucket):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*number_of_bucket/max_value)
        arr[index_b-1].append(j)

    for i in range(number_of_bucket):
        arr[i] = insertion_sort(arr[i])

    k = 0

    for i in range(number_of_bucket):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


# customList = [10, 59, 588, 440, 283]
# print(bucketSort(customList))
