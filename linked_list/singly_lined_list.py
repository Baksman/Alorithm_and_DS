

class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


singleLinkedList = SingleLinkedList()

node1 = Node(10)
node2 = Node(12)


singleLinkedList.head = node1
singleLinkedList.head.next = node2
singleLinkedList.head.tail = node2


    