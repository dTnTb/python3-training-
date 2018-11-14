def rm_empty(s):
    return s and s.strip()
l1 = ['a','','b','x',None,'c','  s  ','         ']
print(list(l1))

print(rm_empty(''))
print()
l2 = list(filter(rm_empty,l1))
print(l2)