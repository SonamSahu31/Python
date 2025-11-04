class person:
    __name = "satyam"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = person()

print(p1.welcome())