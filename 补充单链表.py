a=[1,2,3,5,5]
a=iter(a)
print(next(a))
#单链表是否存在环 设一个n m n每次走两步 m每次走一步 快慢指针
#如果快指针追到了慢指针，那么就存在环
