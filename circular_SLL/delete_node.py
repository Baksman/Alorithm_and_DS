
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CirculaLinkedList:
    head: Node
    tail: Node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break

    def insertCSSL(self, value, location):
        if self.head == None:
            return "The head is referenced to None"
        else:
            if location == 0:
                newNode = Node(value)
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
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        return "The node has been succesfully inserted"

    def createCSLL(self, value):
        newNode = Node(value=value)
        newNode.next = newNode
        self.tail = newNode
        self.head = newNode
        return "Circular linked list has been created"

    def deleteNode(self, location):
        if self.head == None:
        
            print("Error is not any code in CSSL")
            return
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.head.next = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.head.next = None
                self.tail = None
            else:
                node = self.head

                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode


circularSLL = CirculaLinkedList()
print(circularSLL.createCSLL(1))

circularSLL.insertCSSL(0, 0)
circularSLL.insertCSSL(10, 0)
circularSLL.insertCSSL(20, 0)
circularSLL.insertCSSL(30, 0)
circularSLL.insertCSSL(40, 0)
print([node.value for node in circularSLL])
circularSLL.deleteNode(3)
print([node.value for node in circularSLL])
circularSLL.deleteNode(1)

print([node.value for node in circularSLL])
circularSLL.deleteNode(1)
print([node.value for node in circularSLL])

circularSLL.deleteNode(0)
print([node.value for node in circularSLL])

# singleLinkedList = SingleLinkedList()

# singleLinkedList.insertSLL(10, 1)
# singleLinkedList.insertSLL(20, 1)
# singleLinkedList.insertSLL(30, 0)
# singleLinkedList.insertSLL(40, 2)
# # singleLinkedList.insertSLL(0, 8)
# # singleLinkedList.insertSLL(10,1)
# # singleLinkedList.insertSLL(10,1)
