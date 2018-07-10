def merge(left,right):
    b=[]
    while left and right:
        if left[0]<=right[0]:
            b.append(left.pop(0))
        else:
            b.append(right.pop(0))
    while left:
        b.append(left.pop(0))
    while right:
        b.append(right.pop(0))
    return b
def mergeSort(a):
    if len(a)<=1:
        return a
    min_a = len(a)//2
    left = mergeSort(a[:min_a])
    right = mergeSort(a[min_a:])
    return merge(left,right)
a=[14,12,15,13,11,16]
print(mergeSort(a))
print(a)
