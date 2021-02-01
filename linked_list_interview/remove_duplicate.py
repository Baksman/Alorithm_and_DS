from LinkedList import LinkedList


def remove_duplicate(ll):
    if ll == None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])

        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
remove_duplicate(customLL)
print(customLL)
