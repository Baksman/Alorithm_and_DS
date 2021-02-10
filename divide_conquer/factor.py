# 0,1,1,2,3,5,8,13,21,34,55
# e.g sum of 45 
def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2

    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1+subP2+subP3


  
print(numberFactor(6))