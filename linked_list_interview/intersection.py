from LinkedList import LinkedList



def intersection(llA,llB):
    if llA.tail != llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)



    shorter = llA if lenA < lenB else llB
    longer = llA if lenA < lenB else llB

