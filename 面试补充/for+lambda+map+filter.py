Ist = [lambda x:x*i for i in range(3)]
print(Ist[0]([2]))
print([m(2) for m in Ist])
print([m([2]) for m in Ist])
a=[[1,2,3],[4,5,6]]
print(len(a[0]))
print([[r[i] for r in a] for i in range(len(a[0]))])
print("###################")
print([[1] for i in range(3)])
