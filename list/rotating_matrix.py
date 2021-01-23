
import numpy as np


myArray = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])


print(myArray)
def roateMatrix(matrix):
    # lenght of matrix is the nummber if rows
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n -layer - 1
        for i in range(first,last):
            # save top element
            top  = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom elemetn to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top toright
            matrix[i][-layer-1] = top
    return matrix



