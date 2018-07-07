#青蛙可以跳1级，2级，n级
#规律应该是a1=1 a2=2 a3=4 a4=8
#第一种：
fib = lambda n:n if n <2 else 2*fib(n-1)
print(fib(5))
