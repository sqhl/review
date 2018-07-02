def funx():
    x=5
    print(x)
    def funy():
        nonlocal x #闭包类的声明
        x+=1
        return x
    return funy
a=funx()
print(a())

#闭包就是函数中的局部变量可以更具内部函数的变化而变化
def a(x):
    def b(y):
        nonlocal x
        x+=y
        return x
    return b
aa=a(10)
print(aa(1))
print(aa(2))
#看吧 闭包就是这种用处
#闭包用处：装饰器、面向对象、单例模式
