#Part of this code is taken from an example I found online https://realpython.com/lessons/how-and-when-use-str/ 
#when I was trying to understand and find pratical examples of classes, def,__init__ and __str__.
#to help with my learning I extended the code by building on it.
#creating class object and setting it's attributes.
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
#assigning the format that the data will be presented.
    def __str__(self):
        return "You have a {} car that has done {} miles.".format(self.color, self.mileage)
#defining the method
def MyCar():
    color = input("Car Color:")
    mileage = int(input("Mileage:"))
    my_car = Car(color, mileage)
    print(my_car)

print ("Enter details of your car")
#calling the function
my_car = MyCar()


