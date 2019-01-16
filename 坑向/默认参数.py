def add_end(list=[]):
        list.append('END')
        return list

print("例1：")
print("call add_end(1, 2, 3)")
print( add_end([1, 2, 3]) )

print   
print("例2：")
print("call add_end(\"x\", \"y\", \"z\")")
print( add_end(["x", "y", "z"]) )

print("上面两个例子不会出问题")

print
print("试试调用两次add_end不带参数")
print("例3：")
print("call add_end()")
print( add_end() )
print
print("例4：")
print("call add_end() again")
print( add_end() )
print("例4结果不是预期的")
