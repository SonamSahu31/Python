# find the greatest of 3 no entered by the user
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter thired number:"))
d= int(input("Enter forth number:"))

if(a>=b and a>=c and a>=d):
    print("first is greatest")
elif(b>=c and b>=d):
    print("second is greatest")
elif(c>=d):
    print("thired is greatest")            
else:
    print("forth is greatest")   
