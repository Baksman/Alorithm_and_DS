# eucleadian algorithm

def GCD(a, b: int):
    if b == 0:
        return a
    return GCD(b, a % b)


print(GCD(48, 18))
