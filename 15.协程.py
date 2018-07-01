#协程是进阶版，因为不管是python的进程和线程，在处理cpu的调度和切换(用户态和内核态）会
#浪费许许多多的资源，为了解决这个问题，就有了协程，协程是用户可以自己切换控制切换的时
#机，造成快速，节约资源的特点
#最普通的yield
'''
import time
def a():
    while True:
        print("我是a函数")
        yield
        time.sleep(0.5)
def b(A):
    while True:
        print("我是b函数")
        next(A) #next是返回可迭代对象的下一个值
        time.sleep(0.5)
if __name__=='__main__':
    A=a()
    b(A)
'''
#greenlet实现协程案例
'''
from greenlet import greenlet
import time
def test1():
    while True:
        print("我是a函数")
        gr2.switch()
        time.sleep(0.5)
def test2():
    while True:
        print("我是b函数")
        gr1.switch()
        time.sleep(0.5)
def main():
    gr1.switch() #切换到gr1运行
if __name__=="__main__":
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    #main() #开始参数时switch
'''
#gevent实现协程案例
'''
import gevent
def a(n):
    for i in range(n):
        print("这是a函数")
        gevent.sleep(1)
        #time.sleep(1)这是没用的,并不会让gevent感知到等待状态
def b(n):
    for i in range(n):
        print("这是b函数")
        gevent.sleep(1)
def main():
    g1 = gevent.spawn(a,5)  #这里有种和线程一样的使用方法的感觉
    g2 = gevent.spawn(b,5)

    g1.join()
    g2.join()
if __name__=="__main__":
    main()
'''
#gevent使用下载网页信息实现异步IO
#必须要使用cmd运行，解释器始终有问题
#这个可以设置遇到io时，会切换任务，就是那个monkey
import urllib.request
import gevent
from gevent import monkey
monkey.patch_all() #猴子补丁 将普通的涉及IO的操作替换为gevent
def dowload(url):
    print("get %s"%url)
    reponse = urllib.request.urlopen(url)
    data = reponse.read()
    print("下载 %d from %s"%(len(data),url))
def main():
    g1 = gevent.spawn(dowload,"https://www.baidu.com/")
    g2 = gevent.spawn(dowload,"http://www.qq.com/")
    g3 = gevent.spawn(dowload,"http://www.google.cn/")
    gevent.joinall([g1,g2,g3])
if __name__=="__main__":
    main()

