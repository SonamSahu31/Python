#attributes-> kya kya properties h aapke pass
#self -> object ka reference h
class student:
    collage_name = "Global collage"
    name = "satyam" #class attribute

    def __init__(self,name,marks):
       self.name = name #object attr > class attr
       self.marks = marks

s1 = student("sonam",55)
print(s1.name)
print(student.collage_name)