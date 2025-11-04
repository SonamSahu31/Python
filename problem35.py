#create a class that takes name & marks of 3 students as argument in constructer . then create a method to print the average

class student:
    def __init__(self , name , marks):
       self.name = name
       self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your score is :", sum/3)

s1 = student("Satyam sahu", [22,33,54] )
s1.get_avg()
s2 = student("Sonam sahu", [45,33,54] )
s2.get_avg()
        