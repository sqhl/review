class a(object):
    def __init__(self):
        self.__b=1
        self._b=2
        self.__b__=3
A=a()
print(A.__b__) #约定命名方式,防止冲突
print(A._b) #私有，无法使用import导入
print(A._a__b) #这个是约定，想要访问，则需要使用 对象._类名__名称 来访问
