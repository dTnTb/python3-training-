def fib(max):
    n,a,b =0, 0, 1
    while(n<max):
        print(b)
        a,b = b,a+b
        n = n + 1
    return print("done")

fib(1)
fib(5)

def fib_yeild(max):
    n,a,b =0, 0, 1
    while(n<max):
        yield b
        a,b = b,a+b
        n = n + 1
    return print("done")

for n in fib_yeild(5):
    print(n)