#时至三年，又回来了
#快排 快排 快排
'''
def quick_sort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [i for i in a[1:] if i < pivot]
        greater = [j for j in a[1:] if j > pivot]
        print("less",less)
        print("greater",greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)
'''
def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
a=[2,4,6,7,1,2,5]
print(quickSort(a,0,len(a)-1))
#时间复杂度O(n2)
