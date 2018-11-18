from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sel(t):
    return t[1]
L2 = sorted(L,key = sel)
print(L2)