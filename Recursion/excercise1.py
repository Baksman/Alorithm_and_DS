def sum_of_digit(n):
    assert n >0 and int(n) == n , "only positive or ineger needed"
    if n == 0 :
        return n
    return int(n%10)+ sum_of_digit(int(n/10))



print(sum_of_digit(51))