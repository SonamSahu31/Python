#Set -> unordered hota h, duplicate value allowed  nhi hoti h 
# collection = set() #empty set -> right syntax
# print(type(collection))

#union method -> combines both set values & return values
set1 = {1,2,3}
set2 = {4,5,6,2}
print(set1.union(set2))

#intersection method -> combine common value 
print(set1.intersection(set2))