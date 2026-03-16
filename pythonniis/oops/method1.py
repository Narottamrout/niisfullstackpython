class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome",self.name)
    def get_marks(self):
        print("marks",self.marks)
s1=student("rahul",45)
s1.welcome()
s1.get_marks() 