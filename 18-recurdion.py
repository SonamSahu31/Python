def show(n):

    if(n==0): #base case / stopping condition
        return
    print(n)
    show(n-1)
    

show(6)