a={'a':1,'b':2}
#普通查询：
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
#根据value查询key
print(list(a.keys())[list(a.values()).index(2)])
#根据key查value就很简单了

