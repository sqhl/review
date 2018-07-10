#就是一个交叉节点
#思路就是从最后一个节点判断，如果不同证明没有相交，相同则找到相交点，这里是用一个list来
#模拟
'''
a = [1,2,3,7,9,1,5]
b = [4,5,7,9,1,5]
for i in range(1,min(len(a),len(b))):
    if i==1 and (a[-1] != b[-1]):
        print("No")
        break
    else:
        if a[-i] != b[-i]:
            print("交叉节点：",a[-i+1])
            break
        else:
            pass
'''
#下面使用一个class的类来模拟
#了解一下next函数：
a=[1,2,3,4]
next(iter(a))#next可以输出可迭代对象的下一个值
#但凡是可以返回可迭代的对象都可以称之为iterable
