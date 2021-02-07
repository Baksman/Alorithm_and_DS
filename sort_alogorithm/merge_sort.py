

def merge(customList, l, m, r):
    n1 = m - l - 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = customList[l+1]

    for j in range(0, n2):
        R[j] = customList[l+1]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
