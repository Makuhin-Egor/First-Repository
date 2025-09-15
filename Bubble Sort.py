def bs(l):
    a = True
    while a:
        a = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                a = True
    return l

