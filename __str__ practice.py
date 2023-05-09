class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "You have a {} car that has done {} miles.".format(self.color, self.mileage)
    
def MyCar():
    color = input("Car Color:")
    mileage = int(input("Mileage:"))
    my_car = Car(color, mileage)
    print(my_car)

print ("Enter details of your car")
my_car = MyCar()


