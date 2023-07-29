"""Base class vehicle."""
class Vehicle:
  def setVehicleMake(self, Make):
    self.VehicleMake = Make
  def getVehicleMake(self, Make):
    self.VehcileMake = Make  
  def setVehicleModel(self, Model):
    self.VehicleModel = Model
  def getVehicleModel(self, Model):
    self.VehicleModel = Model
  
class Car(Vehicle):
  def setCarDoors(self, Doors):
    self.CarDoors = Doors
  def getCarDoors(self, Doors):
    self.CarDoors = Doors
  def display_option(self):
    print (f"\nThe make of the car is {self.VehicleMake.title()}")
    print (f"\nThe model of the car is {self.VehicleModel.title()}")
    print (f"\nThe car is a {self.CarDoors.title()} door.")
    print ("\nYour car has been added to the garage.")

class Truck(Vehicle):
  def setBedLength(self, BedLength):
    self.BedLength = BedLength
  def display_option(self):
    print (f"\nThe make of the Truck is {self.VehicleMake.title()}.")
    print (f"\nThe truck model is {self.VehicleModel.title()}")
    print (f"\nThe truck bed length is {self.BedLength}.")
    print ("\nYour truck has been added to the garage.") 
    
print("Welcome to the garage.")
print()
while True:
  choices = int(input("\nEnter 1 to make a car, 2 to make a truck, or 3 to exit. " ))
  if choices == 1:
    
    strMake = input("\nPlease enter the make of the car. ") 
    strModel = input("Please enter the model of the car. ")
    strDoors = input("How many doors does the car have? ")
    new_car = Car()
    new_car.setVehicleMake(strMake)
    new_car.getVehicleMake(strMake)
    new_car.setVehicleModel(strModel)
    new_car.getVehicleModel(strModel)
    new_car.setCarDoors(strDoors)
    new_car.getCarDoors(strDoors)
        
    new_car.display_option()
            
   
  elif choices == 2:
    new_truck = Truck()
    strMake = input("Please enter the make of the truck. ")
    new_truck.setVehicleMake(strMake)
    strModel = input("Please enter the truck model. ")
    new_truck.setVehicleModel(strModel)
    strBed = input("Enter the bed length. ")
    new_truck.setBedLength(strBed)
    new_truck.display_option()
  
  elif choices == 3:
    break
print("You you for using our garage today. Please come again.")
  