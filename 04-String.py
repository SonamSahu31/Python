str1 = "this is a string. \n We are creating it in python"
print(str1)
print(len(str1))

#INDEXING
#index -> position milna
ch = str1[1]
print(ch)

#SLICEING
#accessing parts of a string
print(str1[1:5])
print(str1[18:len(str1)]) #last index par jane ke liye len(str) lete h

#NEGATIVE INDEXING
print(str1[-5:-1])

#STRING FUNCTIONS
print(str1.endswith("thon")) #return true or false
print(str1.capitalize())
print(str1.replace("n","m"))
print(str1.replace("python","SQL"))
print(str1.find("python"))
print(str1.count("a"))