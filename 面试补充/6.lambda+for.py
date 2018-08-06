a=[lambda x:x*2 for x in range(3)]
print(a[0])
print(a[0](2))
print(a[0](1))
print(a[0]([1,2]))
print(a[0]([[1],[2]]))
b=[[lambda x:x*2] for x in range(3)]
print(b[0])
print(b[0][0])
print(b[0][0](2))
