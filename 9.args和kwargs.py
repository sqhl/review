def a(*args): #args是接受任意数量的参数
    for i in args:
        print(i)
a(1,2,3)

def b(**kwargs):
    for i in kwargs.items():
        print(i)

b(apple = 'fruit', cabbage = 'vegetable') #kwargs接受命名好的参数传入
#*args必须在**kwargs前面
#调用的时候也可以用这种语法 *和**
def a(b,c,d):
    print(b,c,d)
e=[1,2,3]
a(*e)#当然e中的参数数量必须与a中的传入参数相同才可以
