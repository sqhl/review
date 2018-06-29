#装饰器就是为已存在的对象添加额外的功能
def a(func):
    print(1)
    def b(*args,**kwargs):
        print(2)
        func(*args,**kwargs)
        print(3)
    return b
@a
def c(e,d):
    print(e,d)
c("我","你")
#从这里就可以看出来很多问题
