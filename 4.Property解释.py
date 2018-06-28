#property(fget=None, fset=None, fdel=None, doc=None)
#这是他的四个方法：get，set，del，doc是说明文档
'''
class a(object):
    def __init__(self):
        self.s=1
    @property
    def fangfa(self):
        return self.s
    @fangfa.setter #这个是装饰器的方法 只有在上面的装饰器存在的情况下才可以使用
    def fangfa(self,value):
        self.s=value
    @fangfa.deleter
    def fangfa(self):
        print('属性已删除')
        
A=a()
print(A.fangfa)
A.fangfa = 60
print(A.fangfa) #使用过了setter之后就可以使用这样的东西了
del A.fangfa #调用装饰器中的删除,并不是正真意义上的删除,只是使用del这种方式
'''
#使用非装饰器：
class a(object):
    def __init__(self):
        self.s=1
    def fangfa_get(self):
        return self.s
    def fangfa_set(self,value):
        self.s=value
    def fangfa_del(self):
        print('属性已删除')
    fangfa = property(fangfa_get,fangfa_set,fangfa_del) #是差不多的
        
A=a()
print(A.fangfa)
A.fangfa = 60
print(A.fangfa)
del A.fangfa
