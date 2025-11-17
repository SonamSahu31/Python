def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

num1 = float(input("enter first value : "))
num2 = float(input("enter second value : "))
print("addition")
print("subtraction")
print("multiplecation")
print("division")

person = str(input("select option :"))
# num1 = float(input("enter first value : "))
# num2 = float(input("enter second value : "))

if(person == "add" ):
    print("addition", add(num1 ,num2))
elif(person == "sub" ):
    print("subtraction",sub(num1 , num2))

elif(person == "mul" ):
    print("multiplecation" ,mul(num1 , num2))

elif(person == "div" ):
    print("division", div(num1 , num2))    

else:
    print("invalid")

    



