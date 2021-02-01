
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

    def createCSLL(self, value):
        newNode = Node(value=value)
        newNode.next = newNode
        self.tail = newNode
        self.head = newNode
        return "Circular linked list has been created"









circularSLL = CirculaLinkedList()
print(createCSLL.cerateCSLL(1))

[node.value for node in circularSLL]

# singleLinkedList = SingleLinkedList()

# singleLinkedList.insertSLL(10, 1)
# singleLinkedList.insertSLL(20, 1)
# singleLinkedList.insertSLL(30, 0)
# singleLinkedList.insertSLL(40, 2)
# # singleLinkedList.insertSLL(0, 8)
# # singleLinkedList.insertSLL(10,1)
# # singleLinkedList.insertSLL(10,1)
