

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

    def insert(self, value, location):
        if self.head == None:
            print("node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.previous = None
                newNode.next = self.head
                self.head.previous = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.previous = tempNode
                newNode.next.previous = newNode
                tempNode.next = newNode.next
                


doubleLL = DoubleLinkedList()
doubleLL.creationOfDoubleLinkedList(10)
doubleLL.insert(0,0)
doubleLL.insert(10,1)
doubleLL.insert(80,0)
doubleLL.insert(90,1)


print([node.value for node in doubleLL])
