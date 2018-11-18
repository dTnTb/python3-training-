def gen():
    yield 1
    n = 1
    while 1:
        n = n + 2
        yield n
        print('after yield:'+str(n))

g = gen()
print(next(g))
print('-'*8)
print(next(g))
print('-'*8)
print(next(g))
print('-'*8)
print(next(g))
print('-'*8)