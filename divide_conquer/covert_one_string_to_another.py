
# convert s2 to s1 by deleting,editing,adding
def find_min_operation(s1: str, s2: str, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1+1, index1+1)
    else:
        deleteOp = 1 + find_min_operation(s1, s2, index1, index2+1)
        insertOp = 1 + find_min_operation(s1, s2, index1+1, index2)
        replaceOp = 1 + find_min_operation(s1, s2, index1+1, index2+1)

        return min(deleteOp, insertOp, replaceOp)


print(find_min_operation("table","tbres",0,0))