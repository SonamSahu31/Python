class student:
    #default constructors -> automatic execute ho jata h  
    def __init__(self):
        pass #pass -> baad me value pass karenge agar need hui to
    
    #parameterize constructer -> self ke sath other constructer bhi hote h
    def __init__(self , name, marks):#create a constructer , always pass a self argument
        self.name = name #insant attribute
        self.marks = marks
        print("adding new student")
   

# creating object(instance)
s1 = student("sonam",33)
print(s1.name,s1.marks)

s2 = student("sahu",34)
print(s2.name,s2.marks)