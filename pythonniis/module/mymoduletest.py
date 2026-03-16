a = 10

def show():
    print("This is show function from module")

def add(x, y):
    return x + y
import mymoduletest
mymoduletest.show()
print(mymoduletest.add(10,20))
print(mymoduletest.a)