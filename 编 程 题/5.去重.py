#集合去重
a=list(set([1,2,3,4,2]))
print(a,type(a))
#用字典 这种方法不会保存原有的顺序
l1=['b','c','b','d']
l2={}.fromkeys(l1).keys()
print(l2)
#使用排序了方式来
l2=list(set(l1))
l2.sort(key=l1.index)
print(l2)
#列表推导
l1=[1,2,3,2,4,2]
l2=[]
[l2.append(i) for i in l1 if not i in l2]
print(l2)
