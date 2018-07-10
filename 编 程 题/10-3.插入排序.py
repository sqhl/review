#插入排序
def cha_sort(a):
    len_a=len(a)
    for i in range(1,len_a):
        for j in range(i):
            if a[i]<a[j]:
                a.insert(j,a[i])
                a.pop(i+1)
                break
a=[1,5,2,6,9,3]
cha_sort(a)
print(a)
#也是跟O(n2)差不多的速度 而且很稳定
