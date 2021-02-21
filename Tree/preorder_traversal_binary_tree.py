# types of treversal
# DFS and BFS
# pre-order traversal
# rootNode -->  left subTre --> Right SubTree


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTrevarsal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTrevarsal(rootNode.leftChild)
    preOrderTrevarsal(rootNode.rightChild)


preOrderTrevarsal(newBT)
