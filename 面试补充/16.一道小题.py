#25.有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
#要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
#1. 分别计算a,b序列的和；
#2. 求a序列和与b序列和的差值的一半，记为half；
#3. 在和值大的序列中找出一个与和值小的序列中的元素max的差值最接近half的元素，记为min；
#4. 将max与min互换即可。
from functools import reduce
from operator import mul
#求积 reduce(mul,a)
#求和 sum
def f(a,b):
    ab = abs(sum(a) - sum(b))
    if sum(b)>sum(a):
        a,b=b,a
    flag=0
    for i in range(len(a)):
        max = i
        min_ab = 99999
        for j in range(len(b)):
            if abs(a[i] - b[j] - ab)<min_ab and a[i]>b[j]:
                min_ab = abs(a[i] - b[j] -ab)
                min = j
                print(min_ab)
                if min_ab ==0:
                    flag =1
                    break
        if flag==1:
            break
    a[max],b[min] = b[min],a[max]
    print(a,b)
    print(sum(a),sum(b))
a=[1,2,3,4]
b=[5,6,7,8]
f(a,b)
