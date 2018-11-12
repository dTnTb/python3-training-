# question description
# https://en.wikipedia.org/wiki/Tower_of_Hanoi
def move(n,a,b,c):
    if n == 1:
        print(a + " -> move to " + c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    pass 

move(3,'A','B','C')