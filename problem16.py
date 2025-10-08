#Check if a list contains a palindrom of elements.
#list = [1,2,1]
list = ["m", "a", "a"]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("Not palindrome")