# double = lambda x: x*2
# print(double(5))

#sum of two number
# add = lambda a,b : a+b
# result = add(3,5)
# print("sum", result)

#sum of digit in lambda fumction
from functools import reduce
num = int(input("enter your number "))
digits = list(map(int,str(num)))

sum_of_digits = reduce(lambda x,y: x+y, digits)
print("sum of digits",sum_of_digits)