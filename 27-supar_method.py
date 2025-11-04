class car:
    
    def __init__(self,type):
        self.type = type
    
    @staticmethod #har object par work karti h
    def start():
        print("car started......")

    @staticmethod
    def stop():
        print("car stoped.")

class ToyotaCar(car):
    def __init__(self,name , type):
        super().__init__(type) #super -> parent class ko inherit karta h
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")

print(car1.type)
        
