class Car:
    def __init__(self,brand,model,speed:0):
        self.brand=brand
        self.model=model
        self.speed=speed

    def accelerate(self,amount):
    
        if amount>0: 
            return amount + self.speed

    def brake(self, amount):
    if amount < 0:
        return "Invalid amount"

    if self.speed - amount < 0:
        self.speed = 0
    else:
        self.speed = self.speed - amount

    return self.speed


if __name__=="__main__":
    print("testing the acclerate")
    new_car=Car("Corolla",2002,100)
    print(new_car)
    print(new_car.accelerate(20))
    print(new_car)