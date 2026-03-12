class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def avarage(self):
        avg=(self.marks3+self.marks1+self.marks2)/3
        print("name=",self.name)
        print("avg marks=",avg)
s=student("silu",90,78,56)
s.avarage()