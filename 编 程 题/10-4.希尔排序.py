#希尔排序
def shell_sort(a):
    len_a=len(a)
    gap=len_a//2
    while gap>0:
        for i in range(gap,len_a):
            temp=a[i]
            j=i
            while j>=gap and a[j-gap] >temp:
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap=gap//2
    
a=[1,5,2,6,9,3,2]
#a=[8,9,1,7,2,3,5,4,6,0]
shell_sort(a)
print(a)

#在不停的分组之后，将进行插入排序

