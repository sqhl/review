#单例模式的4中方法
#1.使用__new__这种方法：
#hasattr 判断对象是否含有这个属性
#cls表示类本身，self是一个具体的实例本身
#这里的instance只是一个私有形参,并不具有实际意义
'''
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        print("来看看，调用了几次")
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance
#cls._instance就是一个参数，代表返回父类的__new__这个函数,从始至终都只有一个父类，
#就是为基类添加了一个_instance这个参数
a=Singleton()
a.b=1
print(a.b)
c=Singleton()
print(c.b)
print(c._instance)
'''
#这里我想知道的是:当我们为基类添加了一个参数之后，基类会改变么,这个我准备在__init__和
#new这里做一次比较，经过证明，基类并不会改变，主要是这里想不通当Sington是怎么添加的，
#就是第一个Sington就是父类
####在orm中，Sington的表因该是[Sington,object]所以当他找到自己的时候，发现自己存在
#__new__这个参数，于是乎，进入，但是这里有一个问题是super返回的是基类的__new__()
#基类只存在这一个么

#这里来看看super返回的内存地址：
'''
class a(object):
    def __new__(cls,*args,**kwargs):
        print(id(super(a,cls))) #继承父类和返回__new__的空间是不相同的
        cls._h=super(a,cls).__new__(cls,*args,**kwargs)
        return super(a,cls).__new__(cls,*args,**kwargs)
bb=a()
print(bb._h) #表示当调用了super之后,程序会分配一个单独的地址给cls._h的__new__
             #来单独保存这个函数
print(bb)
bb.aa=1
cc=a()
print(cc._h)
#print(cc.aa) cc没有aa
class b(object):
    def __new__(cls,*args,**kwargs):
        print(id(super(b,cls)))
        return super(b,cls).__new__(cls,*args,**kwargs)
dd=b()
'''
##print(dd.aa) dd同样没有aa
#得到结论,基类确实只存在一个,但是当我们调用基类的__new__这个函数的时候,程序就会开辟一个
#新的空间来保存这个新参的值,于是就可以设计单例模式和节省空间资源了

#2.使用共享属性,这里只有类是增加了内存地址，每一个对象都不同，只不过他们的属性相同,
#同时他们的__dict__都指向了同一个static地址
'''
class a(object):
    _state = {}
    print(1)
    def __new__(cls,*args,**kwargs):
        ob = super(a,cls).__new__(cls,*args,**kwargs)
        ob.__dict__ = cls._state #基本上大多数类都有__dict__属性
        print(cls._state,id(cls._state)) #cls._state就是共享属性
        return ob
b=a()
b.aa=1
c=a()
print(c.aa)
'''
#这里比较理解了,就是这个类变量,是只对类a这个的变量，只会改变
#类变量只针对这个变量对象，后面的类改变了这个类变量,
#都会改变所有类的类变量
#__new__是一个静态方法
'''
class a(object):
    aa=10
    print(1)
    @staticmethod
    def test(self):
        a.aa-=1
#a().aa-=1
bb=a()
print(bb.aa)
#bb.test(bb)
print(bb.aa)
cc=a()
print(cc.aa)
print(id(bb),id(cc))
print(id(bb.aa),id(cc.aa))
'''
#3.装饰器版本的单例模式，坑：不能被继承
#就是进入装饰器，判断存在这个类的实例么，不存在则创建，存在则返回原本的类
def Singleton(cls):
    instances = {}
    def _singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton
@Singleton
class a(object):
    def __init__(self,*args):
        self.a=2
bb=a()
bb.a=3
cc=a()
print(id(bb),id(cc))
print(bb.a,cc.a)
#4.使用imort单例模式,当我们在使用这个的时候，python会将模块写入到.py当中，也就是说
#理解
#将一个类写成：
class singleton(object):
    def foo(self):
        pass
Singleton=singleton()
#放到一个单独文件中
#在主文件中使用import调用即可
