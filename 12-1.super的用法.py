#super使用来继承父类的方法
#super(b,type(类似于self或者cls)).函数 可以在我们重写了子类的函数后调用父类的函数

class a(object):
    def __init__(self):
        print(1)
        print(2)
class b(a):
    def __init__(self):
        print(3)
        super(b,self).__init__()
        print(4)
B=b()

#mro表，类的解析顺序表

print(b.mro())

#super的源码：就是调用了cls在mro中的下一个表
#mro的准则是基类永远在派生类后面
def super(cls,inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls)+1]
