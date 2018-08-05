class test():
    name = "adsda"
    def run(self):
        return "111"
t=test()
print(hasattr(t,"name")) #获取属性,返回True，False
print(getattr(t,"name")) #获取属性名称
print(setattr(t,"age","11")) #设置属性
print(t.age)
t.name = "222"
t1 = test()
print(t1.name)

