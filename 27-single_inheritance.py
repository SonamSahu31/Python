class car:
    color = "balack"
    #car object use nhi ho rahi h isiliye static banaya h
    @staticmethod
    def start():
        print("car started......")

    @staticmethod
    def stop():
        print("car stoped.")

class ToyotaCar(car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start()) 

print(car1.color)
        
