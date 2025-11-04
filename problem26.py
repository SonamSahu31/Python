x = int(input("enter your number :"))

num = (1,4,9,16,25,36,49,64,81,100)

i=0
while i < len(num):
    if(num[i] == x):
        print("found at idx" ,i)
        break
    else:  
        print("finding....")  
    i += 1