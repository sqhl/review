#实体类：实例可以调用,但是类不可以调用
'''
class a(object):
    def __init__(self,x):
        self.x=x
    def foo(self):
        print(1)
class b(a):
    def __init__(self,x,y):
        #a.foo(self,x)
        a.__init__(self,x) #当我们想要覆盖父类中的方法，同时也想调用被覆盖的方法,可以这样
        self.y=y
    def fangfa(self):
        print(self.x+self.y)
c=b(1,2)
c.fangfa()
#a().foo() #实体方法不可以被类调用
'''
#类方法：cls为第一个参数,数约定俗成的,类可以调用,实例也可以调用
'''
class c(object):
    @classmethod #这样创建更加的简单
    def abc(cls):
        print(cls.__name__) #返回类的名称
    #abc = classmethod(abc) #通过这种方式可以创建类方法
a=c()
a.abc()
c().abc()
'''
#静态方法：类和实例都可以调用,静态方法没有默认参数
'''
class c(object):
    @staticmethod #这样创建更加的简单
    def abc(x): #但是我们也可以加参数
        print(x) #返回类的名称
    #abc = staticmethod(abc) #通过这种方式可以创建类方法
a=c()
a.abc(1)
c().abc(0)
'''

