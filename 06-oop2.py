class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        print(f'Hello {name} mark is :')
        

    def add_mark(self,mark):
        self.marks.append(mark)
        
    def get_marks(self):
        return (self.marks)

    def get_avg(self):
        return (sum(self.marks))
    
s1 = Student('firas')
print(s1.name)

s1.add_mark(24)
s1.add_mark(70)
s1.add_mark(90)
print(s1.get_avg())

s2 = Student('Jad')
s2.add_mark(24)
s2.add_mark(70)
s2.add_mark(90)
s1.get_marks()
print(s2.get_avg())
