
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CirculaLinkedList:
    head: Node
    tail: Node

    # def __init__(self):
    #     self.head = None
    #     self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    def cerateCSLL(self, value):
        newNode = Node(value=value)
        newNode.next = newNode
        self.tail = newNode
        self.head = newNode
        return "Circular linked list has been created"

    def insertCSSL(self, value, location):
        if self.head == None:
            return "The head is referenced to None"
        else:
            newNode = Node(value)
            if location == 0:
               
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                self.tail.next = newNode
                newNode.next = self.head
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        return "The node has been succesfully inserted"

    def searchSCLL(self,nodeValue):
        if self.head is None:
            return "There is no any node in this linedllist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return nodeValue
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in CSLL"
                








circularSLL = CirculaLinkedList()
print(circularSLL.cerateCSLL(1))

[node.value for node in circularSLL]



circularSLL.insertCSSL(10, 1)
circularSLL.insertCSSL(20, 1)
circularSLL.insertCSSL(30, 0)
circularSLL.insertCSSL(40, 2)

print(circularSLL.searchSCLL(100))
# singleLinkedList.insertSLL(0, 8)
# # singleLinkedList.insertSLL(10,1)
# # singleLinkedList.insertSLL(10,1)
