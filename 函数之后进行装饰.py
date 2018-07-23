def a(func):
    func()
    def b():
        print(1)
        print(2)
    return b
@a
def c():
    print(3)

c()
