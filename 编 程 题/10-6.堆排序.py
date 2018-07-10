import random

def MAX_Heapify(heap,HeapSize,root,b):#在堆中做结构调整使得父节点的值大于子节点
    print(b+"二叉树：",heap)
    print(HeapSize,"   ",root)
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]h b 
        MAX_Heapify(heap, HeapSize, larger,b)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i,"建造")

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0,"最后")
    return heap

if __name__ == '__main__':
    a = [3,0,5,7,2,8,4,0,8]
    print(a)
    HeapSort(a)
    print(a)
    '''
    b = [random.randint(1,1000) for i in range(1000)]
    #print b
    HeapSort(b)
    print(b)
    '''
#range(start,stop,step) #就是这样 range(1,-1,-1) 得到[1,0]
