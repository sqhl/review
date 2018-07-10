def c_sort(a):
    len_a=len(a)
    for i in range(len_a):
        min_i=i
        for j in range(i+1,len_a):
            if a[j]<a[min_i]:
                min_i=j
        a[i],a[min_i]=a[min_i],a[i]
a=[2,4,6,7,1,2,5]
c_sort(a)
print(a)
#选择排序和冒泡类似，都是O(n2)
