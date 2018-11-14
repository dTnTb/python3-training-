def odd():
    n = 1
    while 1:
        n = n+2
        yield n
def rm(x):
    n = 2
    while n<x:
        if(x%n == 0):
            return False
    return True

l1 = odd()
l2 = list(filter(rm,l1))

for n in l2:
    if(n<100):
        print(n)
    else:
        break