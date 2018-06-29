class a():
    def f(self):
        print("A")
class b(a):
    def f2(self):
        pass
class c(a):
    def f(self):
        print("C")
class d(b,c):
    pass
e=d()
e.f()
##广度：
#这里也是从d开始找,但是没有找到f(),于是返回到b上面去找,b也没有找到,于是找到c,c里面找到，
#就返回

##深度：
#从d开始，找到b，b也没有，但是b继承了a，找到a，a存在，则返回A
