#1.描述yeild的作用：
#把偶才能当前的断点，暂停执行，将函数挂起
#将yeild后的值作为函数返回值返回，可以使用next(),send(),让函数从断点继续执行，唤醒
#函数
def f(n):
    for i in range(n):
        yield i
b=f(5)
print(next(b))
print(b.send(3))
