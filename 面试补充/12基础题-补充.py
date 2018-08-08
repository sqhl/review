#函数dict创建一个字典
#zip是将((a),(b))构建成为[(a,b)]这样的元组，构造好的参数与最短列表一致
#下面这种方式是使用映射的方式来构建
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
A1 = range(10)#[0,1,2,3,4,5,6,7,8,9]
print(A1)
A2 = [i for i in A1 if i in A0]#[] 默认是搜dict的key值 #values()/keys()
print(A2)
A3 = [A0[s] for s in A0] #[1,2,3,4,5]
print(A3)
A4 = [i for i in A1 if i in A3] #[1,2,3,4,5]
print(A4)
A5 = {i:i*i for i in A1} #{0:0,1,1,2,4,3,9...9,81}
print(A5)
A6 = [[i,i*i] for i in A1] #[[0,0],...[9,81]]
print(A6)
#补充：a[-1] 是输出len-1的参数个数

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2) #[0,1]
f(3,[3,2,1]) #[3,2,1,0,1,4]
f(3)#[0,1,4]

#format
# 格式限定符
# 它有着丰富的的“格式限定符”（语法是{}中带:号），比如：
# 填充与对齐
# 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
# 精度与类型f
# 精度常跟类型f一起使用
#主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制
print('{0},{1}'.format('zhangk', 32))
print('{},{},{}'.format('zhangk','boy',32))
print('{name},{sex},{age}'.format(age=32,sex='male',name='zhangk'))
#函数被定义的时候，表达式是用默认参数被计算，而不是它被调用的时候，
#默认列表在函数被定义时候只创建一次

def f(x,l=[]):
    for i in range(x):
        l.append(i)
    print(id(l))
    print(l)
f(2)
f(3,[3,2,1])
f(3)
