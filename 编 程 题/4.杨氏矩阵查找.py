#在一个二维数组中，横竖都是从小到大递增排序，查找一个数字，怎么查找才可以

def find_num(a,b):
    w = len(a)
    h = len(a[0])
    i=0
    j=h-1
    while i<w and j>=0:
        print(a[i][j])
        if int(a[i][j]) == int(b):
            return True
        elif int(a[i][j]) < int(b):
            i+=1
        else:
            j-=1
    return False
'''
a=[[1,3,4,5],[2,4,7,8],[6,7,8,9],[10,11,12,13]]
print(a)
while True:
    b=input("请输入数字：")
    print("要查找的数字：",b)
    print(find_num(a,b))
'''
#这里因为输入没有c的舒服，所以寻找极致的舒服输入
import numpy as np
a=[]
w,h=input("请输入矩阵的长宽：").split()
print(w,h)
for i in range(int(w)):
    a.append(input())
    a[i]=a[i].split(" ")

a=np.array(a)
a.shape=(int(w),int(h))
print(type(a))
print(a)
b=input("输入要寻找的数字：")
print(find_num(a,b))
    
