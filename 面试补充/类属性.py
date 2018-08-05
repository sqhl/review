class a():
    aa=10
t1 = a()
t2 = a()
print(t1.aa,t2.aa,a.aa)
print(t1.__dict__,t2.__dict__,a.__dict__) #这里可以看出来，aa是保存在类a中得
t1.aa+=1
print(t1.aa,t2.aa,a.aa)
print(t1.__dict__,t2.__dict__,a.__dict__) #这里可以看出 t1得aa是11
#在python2中t1的值是1，这里可能改变了类的状态
a.aa +=2
print(t1.aa,t2.aa,a.aa)

#这里可以看出来 类属性可以通过类来调用，改变所有实例类中的值

#    a
#  ------
#  |    |
#  t1   t2
#查找属性值得时候，是向上查找得，所以当我们改变了a得属性值时，会改变t1，t2得值
