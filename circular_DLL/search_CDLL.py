
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class CircularDoubleLinkedList:
    head: Node
    tail: Node

    # def __init__(self):
    #     self.head = None
    #     self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    def cerateCDLL(self, value):
        newNode = Node(value=value)
        newNode.next = newNode
        newNode.previous = newNode
        self.tail = newNode
        self.head = newNode
        return "Circular double linked list has been created"

    def insertCDLL(self, value, location):
        if self.head == None:
            return "Circular double LL doesnt exist"
        else:
            newNode = Node(value=value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.previous = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.previous = self.tail
                self.tail.next = newNode
                self.head.previous = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.previous = tempNode
                newNode.next.previous = newNode
                tempNode.next = newNode
            return "the node has been successfully updated"

    def searchNodeCDLL(self, value):
        if self.head == None:
            return "Theres no any element in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    print(value)
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value doesnt exist"
                tempNode = tempNode.next


circularDLL = CircularDoubleLinkedList()
print(circularDLL.cerateCDLL(2))

circularDLL.insertCDLL(10, 1)
circularDLL.insertCDLL(20, 1)
circularDLL.insertCDLL(30, 0)
circularDLL.insertCDLL(40, 2)
# singleLinkedList.insertSLL(0, 8)
# singleLinkedList.insertSLL(10,1)
# circularDLL.reverseTraverseCDLL()
# singleLinkedList.insertSLL(10,1)
# print([node.value for node in circularDLL])

print(circularDLL.searchNodeCDLL(20))
