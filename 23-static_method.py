#STATIC METHOD -> method thet don't use the self parameter(work at class level)
class student:
    @staticmethod #decorater
    def college():
     print("global")
print(student.college())
