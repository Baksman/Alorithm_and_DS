
# AVL trees are types of BST
# is a self balancing BST
# rotation is the form of balancing AVL

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


newAVLTree = AVLNode(10)
