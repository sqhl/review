l=[x*x for x in range(3)]#迭代器
print(l)
L=(x*x for x in range(3))#生成器
print(L)
for i in L:
    print(i)
