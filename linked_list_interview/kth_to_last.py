from LinkedList import LinkedList


def nthFromLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


customLL = LinkedList()
print(customLL.generate(10, 0, 20))

print(nthFromLast(customLL,4))