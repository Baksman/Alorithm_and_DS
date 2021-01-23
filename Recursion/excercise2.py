def power(base,exp):
    assert int(exp) ==exp, "only integer are alllowed as "
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base,exp - 1)


   