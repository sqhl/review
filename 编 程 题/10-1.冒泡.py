def p_sort(a):
    len_a=len(a)
    for i in range(len_a):
        for j in range(i,len_a):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

a=[2,4,6,7,1,2,5]
p_sort(a)
print(a)
#冒泡就是如此的简单
#时间复杂度O(n2) 
#n-1 + n-2 ....+1 = ((n-1)+1)*(n-1)/2
#(n2-n)/2
#当n很大的时候，忽略-n
#忽略他的系数0.5，就是O(n2)

