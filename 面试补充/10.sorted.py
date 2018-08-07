#sorted(iterable, key=None, reverse=False)  
a=[1,2,3,4,4,3,2,1]
print(sorted(a))
print(sorted(['1','33','111','40'])) #对字符串排序，会从开始依次比较字符的大小，而不是
#返回字符串的长度的比较大小

#sorted(iterable,[key],reserve=False)
#reverse=False(默认)升序 为True为降序

L=[('b',2),('a',1),('c',3),('d',4)]
print(sorted(L, key=lambda x:x[1],reverse=True))

##sort
a.sort()
print(a)
#sort作用在原来的list上，而sorted是作用在一个新list上
