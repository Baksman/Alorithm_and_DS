
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
            node = node.next
            if node.next == self.tail.next:
                break

    def cerateCDLL(self, value):
        newNode = Node(value=value)
        newNode.next = newNode
        newNode.previous = newNode
        self.tail = newNode
        self.head = newNode
        return "Circular double linked list has been created"

    def inserDLL(self,value,location):
        if self.head == None:
            return "Circular double LL doesnt exist"
        else:
            newNode = Node(value=value)
            if location == 0:
                









circularSLL = CircularDoubleLinkedList()
print(circularSLL.cerateCDLL(1))

print([node.value for node in circularSLL])

# singleLinkedList = SingleLinkedList()

# singleLinkedList.insertSLL(10, 1)
# singleLinkedList.insertSLL(20, 1)
# singleLinkedList.insertSLL(30, 0)
# singleLinkedList.insertSLL(40, 2)
# # singleLinkedList.insertSLL(0, 8)
# # singleLinkedList.insertSLL(10,1)
# # singleLinkedList.insertSLL(10,1)
