def count():
    def f(j):
        return lambda :j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) 
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

def count1():
    fs = []
    for i in range(1, 4):
        fs.append(lambda:i*i) 
    return fs
f1,f2,f3 = count1()
print(f1(),f2(),f3())