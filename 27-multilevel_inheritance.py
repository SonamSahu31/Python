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
    def __init__(self,brand):
        self.brand = brand

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = fortuner("diesel")
car1.start()
