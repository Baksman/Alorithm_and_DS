
def permuntation(list1, list2):
    print(list1)
    print(list2.reverse())
    if list1 == list2:   # if list1 == list2.reverse() -- false
        return True
    else:
        return False