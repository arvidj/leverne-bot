
def chunk(ls, n):
    i = 0
    for i in range(0, len(ls), n):
        c = ls[i:][:n]
        yield c
