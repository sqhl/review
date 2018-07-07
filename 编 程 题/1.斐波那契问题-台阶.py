#一直青蛙可以跳上1级台阶，也可以跳上2级台阶，试问，有几种跳法
#之所以是用斐波那契，是因为第一个台阶a1=1 a2=2 a3=3 a4=5 a5=8，所以懂了吧
'''
#第一种lambda
fib = lambda n:n if n <=2 else fib(n-1) + fib(n-2) #等于第四种方法 递归
print(fib(3))
#第二种 #类似于递归
def memo(func):
    cache={}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def fib(i):
    if i <2:
        return 1
    return fib(i-1) + fib(i-2)
print(fib(4))
'''
#第三种 循环
#0 ： a=0 b=1 1个台阶
#1 ： a=1 b=2 2个台阶
#n-1 : a=fib(n-1) b=fib(n)
#n: a=fib(n) b=fib(n+1)
def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b = b,a+b
    return b
print(fib(5))

'''
#第四种 递归 不建议 会超时
def fib(n):
    if n <=2:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(4))
'''

