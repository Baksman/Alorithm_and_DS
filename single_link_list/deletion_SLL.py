

class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value=value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
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

    def deleteNode(self,location):
        if self.head == None:
            print("The singly linedlist does notexist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head

                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            # if the node is neither last nor mid 
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next










class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


singleLinkedList = SingleLinkedList()

singleLinkedList.insertSLL(10, 1)
singleLinkedList.insertSLL(20, 1)
singleLinkedList.insertSLL(30, 0)
singleLinkedList.insertSLL(40, 2)
# singleLinkedList.insertSLL(0, 8)
# singleLinkedList.insertSLL(10,1)
# singleLinkedList.insertSLL(10,1)
singleLinkedList.deleteNode(2)

print([node.value for node in singleLinkedList])
