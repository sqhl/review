#可变类型：list,dict,set
def a(c):
    print("got: ",c)
    c.append(1)
    print("change: ",c)
c=[]
print("kaishi:" ,c)
a(c)
print("jieshu: ",c)
#不可变类型：numbers,strings,tuples
def a(c):
    print("got: ",c)
    c="i/'m second"
    print("change: ",c)
c="i/'m frist"
print("开始：",c)
a(c)
print("结束：",c)
