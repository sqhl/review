#四种方法：
#__new__:会调用多次__init__函数
#共享变量：会调用多次__init__函数
#装饰器：不能够继承
#import：这个需要写在一个其他的模块中导入，同时不能继承，也会触发__init__
#最完美的方案，是调用__init__和共享变量一起来解决这个问题：
#初始化标志和实例绑定
#记住这个 能用就好
class Singleton(object):
    _instances = {}

    def __new__(cls, *args):
        if not cls._instances.get(cls):
            orig = super(Singleton, cls)
            obj = orig.__new__(cls, *args)
            cls._instances[cls] = dict(obj=obj, init=False)
            setattr(cls, '__init__', cls.decorate_init(cls.__init__))
        return cls._instances[cls]['obj']

    @classmethod
    def decorate_init(cls, fun):
        def warp_init(*args):
            if not cls._instances.get(cls):
                return fun(*args)
            elif not cls._instances[cls].get('init', False):
                fun(*args)
                cls._instances[cls]['init'] = True
        return warp_init


class TestSingleton(Singleton):
    def __init__(self):
        print('----TestSingleton --init ------')

print(id(TestSingleton()))
print(id(TestSingleton()))
