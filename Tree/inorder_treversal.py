# left subTre --> rootNode --> Right SUbTree


class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



def inorderTraversal(rootNode):
    if not rootNode:
        return;

    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)
    


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

inorderTraversal(newBT)