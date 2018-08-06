Ist = [lambda x:x*i for i in range(3)]
print(Ist[0]([2]))
print([m(2) for m in Ist])
print([m([2]) for m in Ist])
a=[[1,2,3],[4,5,6]]
print(len(a[0]))
print([[r[i] for r in a] for i in range(len(a[0]))])
print("###################")
print([[1] for i in range(3)])
#可能时闭包原理
lst = [lambda x:x*i for i in range(4)]
print([m(2) for m in lst]) #这个i是全局的，lambda里面保留的引用

#[6, 6, 6, 6]
