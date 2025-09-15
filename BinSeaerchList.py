def BinSL(s):
    s.sort()
    n = int(input('Вевдите число для поиска: '))
    l = -1
    r = len(s)
    while r > l + 1:
        m = (l + r) // 2
        if n >= s[m]:
            l = m
        else:
            r = m
    if s[l] == n:
         return(f'The position is {l}')
    else:
        return('Not found')
