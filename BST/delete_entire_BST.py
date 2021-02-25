

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    # if its empty
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfull inserted"


def minimmNode(bstNode: BSTNode):
    currentNode = bstNode
    while(currentNode.leftChild is not None):
        currentNode = currentNode.leftChild
    return currentNode


def deleteNode(rootNode: BSTNode, value):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.leftChild, value)
    else:
        if rootNode.leftChild == None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode
        if rootNode.rightChild == None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode

        # if node has two children
        # successor is the smallest in the right subTree
        tempNode = minimmNode(rootNode.rightChild)
        rootNode.data = tempNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, tempNode.data)

def deleteBST(rootNode: BSTNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BST has been deleted"


newBST = BSTNode(None)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
