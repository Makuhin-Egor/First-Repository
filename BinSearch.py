def BinS(l, r):
    print('Your answers should be y/n (Yes or No)')
    while l < r:
        m = (l + r) // 2
        a = input(f'x > {m}?')
        if a == 'y':
            l = m + 1
        else:
            r = m
    return(f'x = {l}')
