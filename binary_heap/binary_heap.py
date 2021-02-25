# every node except the last node must be completel filled i.e have two children

# the value of  any given node must be less than the value od its children

# e.g prims algorithm,Heap sort,Priority queue
# types , max and min heap
# peek of heap is the root of heap index 1 for arraybased


class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peek(rootNode: Heap):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def sizeOfHeap(rootNode: Heap):
    if not rootNode:
        return
    return rootNode.heapSize


def levelOrde(rootNode: Heap):
    if not rootNode:
        return
    else:
        # we are not storing any element at 0 index
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])


def heapifyExtract(rootNode: Heap, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2+1
    swapChild = 0

    if rootNode.index < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                tempNode = rootNode.customList[index]
                rootNode.customList[leftIndex] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = tempNode
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                tempNode = rootNode.customList[index]
                rootNode.customList[leftIndex] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = tempNode
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                tempNode = rootNode.customList[index]
                rootNode.customList[leftIndex] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = tempNode
    heapifyExtract(rootNode, swapChild, heapType)


def extractNode(rootNode: Heap, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType,)
        return extractedNode


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,5,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,1,"Max")
