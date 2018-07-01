def consume(name):
    print("要开始吃了")
    while True:
        print("[consumer] %s 等待" % name)
        bone = yield
        print("[%s] 正在啃骨头 %s" % (name, bone))
def producer(obj1,obj2):
    obj1.send(None)
    obj2.send(None)
    print("-------------------")
    n=0
    while n<5:
        n+=1
        print("[producer]  正在生产骨头 %s" % n)
        obj1.send(n)
        obj2.send(n)
if __name__=="__main__":
    con1 = consume("消费者A")
    con2 = consume("消费者B")
    producer(con1,con2)
