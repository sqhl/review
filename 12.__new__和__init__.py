#__init__和__new__的区别,前面的是实例方法,后面的是静态类
#__new__方法会返回一个创建的实例,而__init__什么都不返回
#只有在__new__返回一个cls的实例时后面的__init__才能被调用
#当创建一个新实例时调用__new__,初始化一个实例时用__init__

#上一节当中我们有讲到新式类，这个就是新式类的东西
#测试，一直不满意new的使用方式
class a(object):
    def __init__(self):
        self.b=2
    def __new__(cls,*args,**kwargs):
        print("啦啦啦啦，输出一次表示我调用了一次")
        return super(a,cls).__new__(cls,*args,**kwargs)
class b(a):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_h"):
            print("开始的时候")
            cls._h=super(b,cls).__new__(cls,*args,**kwargs)
            print("结束的时候")
        return cls._h
bb=b() #if not hasattr这个函数只会调用一次
print(bb.b)
bb.b=1
bb.c=4
print(bb.b)
cc=b() #这里当我们调用b()的时，原来的self.b又被初始化了一次,所以又变成了2
print(cc.b)
print(bb.c)#这里的c存在并且输出为4表示我们的单例模式是成功的
try:
    print(a()._h)
except:
    print("不存在a()._h这个值")
#我记得我们说过cls是代表这个类本身，cls._h则是代表返回到最终的父类__new__，同一个父亲



#在类被初始化之前，先调用的是__new__这个方法,然后再是调用了__init__这个方法
#他也会通过广度来寻找到一个__new__，所有类都具有最基础的__new__，存在于object这个
#基类当中

##cls代表了当前类
##slef代表了当前实例


#这个地方的__del__方法是因为代码结束了,程序回收资源的时候才执行的,没有执行__init__
#因为__new__没有返回实例
class Dog (object):
    def __init__(self):
        print("-----init方法-----")
    def __del__(self):
        print("-----del方法-----")
    def __str__(self):
        #print("-----str方法-----")
        return ("-----str方法-----")
    def __new__(cls):
        print("-----new方法-----")
        object.__new__(cls)
        
xtq = Dog()

