
def fib(n):
    assert n > 0 and int(n) == n ,"fibonnaci number cannot be negative"
    if n in [0,1]:
        return n
    # assert n > 0 ,"cant be less than zero"
    return fib(n-1) + fib(n-2)  



print(fib(1.5))