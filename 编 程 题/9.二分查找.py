def search(a,b):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)//2
        guess = a[mid]
        if guess>b:
            high=mid-1
        elif guess<b:
            low=mid+1
        else:
            return mid
    return None
a=[1,3,5,7,9]
print(search(a,2))
#就是改变low和high的值 让他们找中间的值就可以了
