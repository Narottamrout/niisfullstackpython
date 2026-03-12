
class person:
    def f1(self):
        print("class person")
class student(person):
    def f2(self):
        print("class student")
class engineer(student):
    def f3(self):
        print("class engineering")
obj = engineer()
obj.f1()
obj.f2()
obj.f3()
obj = person()
obj.f1()

obj1 = student()
obj1.f1()
obj1.f2()

obj2 = engineer()
obj2.f1()
obj2.f2()
obj2.f3()        