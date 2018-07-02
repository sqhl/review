#简单，不会浪费空间来保存，它只会计算，不会像声请一个函数一样占用内存空间
#过滤器：filter：调用bool来遍历每个元素，返回一个为true的序列
a = [1,2,3,4,5,6,7]
b = filter(lambda x: x > 5, a)
print(list(b))
#map是对序列的每个项都执行函数
c = map(lambda x:x*2,[1,2,3])
print(list(c))
#reduce函数是对一个序列的每个迭代调用函数，下面是求3的阶乘
from functools import reduce
print(reduce(lambda x,y:x*y,range(1,4)))
