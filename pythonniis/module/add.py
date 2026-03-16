a = 100
def add(x, y):
    return x + y

def show():
    print("This is show function from module")

import mymoduletest
mymoduletest.show()
print(mymoduletest.add(10,20))
print(mymoduletest.a)