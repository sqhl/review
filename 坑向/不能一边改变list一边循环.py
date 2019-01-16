import copy

lis = [1, 2, 3, 5, 4, 2, 3, 8, 9, 4, 1]
a = copy.copy(lis)
for i in lis:
    while a.count(i) >= 2:
        a.remove(i)
print(a)

# 
