#list:
#首先在声请空间的时候，list会申请较大的空间避免加入新元素之后都要调用realloc进行内存
#分配
#list的append:list大小申请：0，4，8，16，25这样申请空间，避免多次调用
#list的insert：在处理的时候，比如说a=[1,2,3,4,5] a.insert(1,5) 会将a[1]存为5，然后
#所有值都赋值为新的元素，时间复杂度O(n)
#list的pop：弹出最后一个元素：减小当前list的申请空间，时间复杂度O(1)
#list的remove：移除指定位置元素，也是相似于insert，时间复杂度O(n),并且空间大小会减小
#核心
'''
调整后大小 (new_allocated) = 新元素数量 (newsize) + 预留空间 (new_allocated)
调整后的空间肯定能存储 newsize 个元素。要关注的是预留空间的增长状况。
将预留算法改成 Python 版就更清楚了:(newsize // 8) + (newsize < 9 and 3 or 6)。
当 newsize >= allocated,自然按照这个新的长度 "扩容" 内存。
而如果 newsize < allocated,且利用率低于一半呢?
allocated    newsize       new_size + new_allocated
10           4             4 + 3
20           9             9 + 7
很显然,这个新长度小于原来的已分配空间长度,自然会导致 realloc 收缩内存。(不容易啊)
'''



#is是比较地址 而 ==是比较值


#read和readline和readlines
with open("备忘录.txt","r") as f:
    print(f.readline())
    print("--------------")
    print(f.readlines())
    print("--------------")
    f.seek(0)
    print(f.read())
#seek(x,0) 第二个位置0：起始位置 1：当前位置 2：末尾
#x为从那个位置的那个字符，偏移量
