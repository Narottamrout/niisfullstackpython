class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_person(self):
        print("name",self.name)
        print("age",self.age)
s=person("silu",45)
s.show_person()        