# method -> jo function class ke ander likhe jate h unko ham method kahte h
class student:
    collage_name = "Global collage"

    def __init__(self,name,marks):
       self.name = name 
       self.marks = marks

    def welcome(self):
        print("welcome student" , self.name) 

    def get_marks(self):
        return self.marks      

s1 = student("sonam",55)
print(s1.name)
print(student.collage_name)
s1.welcome()
print(s1.get_marks())