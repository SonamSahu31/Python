student = {
    "name" : "Sonam Sahu",
    "subject" : {
        "eng" : 40,
        "computer" : 70,
        "math" : 60,
    }
}
#nested dictionary
# print(student["subject"]["eng"])
# #keys
# print(student.keys())
# #type casting
# print(list(student.keys()))

# print(len(student)) #total number of key values

#values dictionary
#print(student.values()) # return all values

#items dictionary
#print(student.items()) #tuples return hote h

# get dictionary -> return the key according value
#print(student["name2"]) #error
#print(student.get("name2")) #no error -> None

# update dictionary -> insert the new dict
student.update({"city" : "delhi"})
print(student)