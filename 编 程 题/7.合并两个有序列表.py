#有两个数组，求有序合并的快速方法
#递归的方法没写，但是都是差不多的
#这个是循环的方法
def find_new_list(a,b):
    new=[]
    while len(a)>0 and len(b)>0:
        if a[0]<=b[0]:
            new.append(a.pop(0))
        else:
            new.append(b.pop(0))
    new.extend(a)
    new.extend(b)
    return new

a=[1,2,3,7]
b=[3,4,5]
print(find_new_list(a,b))
