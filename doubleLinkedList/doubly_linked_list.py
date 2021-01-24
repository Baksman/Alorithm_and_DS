

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next

    def creationOfDoubleLinkedList(self, value):
        node = Node(value=value)
        node.previous = None
        node.next = None
        self.head = node
        self.tail = node
        return "The double linked list is created succesfully"


doubleLL = DoubleLinkedList()
doubleLL.creationOfDoubleLinkedList(10)
print([node.value for node in doubleLL])
