# left-->right subTree-->rootNode
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def postOrderTrevarsal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    postOrderTrevarsal(rootNode.leftChild)
    postOrderTrevarsal(rootNode.rightChild)
    print(rootNode.data)


postOrderTrevarsal(newBT)
