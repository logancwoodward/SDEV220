"""Logan Woodward
SDEV 220
4/8/24
M03 Lab Case Study
App name: Logan's Car Information App v1.0

    Write a Python app that has the following classes:
    A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
    A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
    year
    make
    model
    doors (2 or 4)
    roof (solid or sun roof).
    Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
    The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
    The app will then output the data in an easy-to-read and understandable format, such as this:
    Vehicle type: car
    Year: 2022
    Make: Toyota
    Model: Corolla
    Number of doors: 4
    Type of roof: sun roof"""


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}\n" \
               f"Year: {self.year}\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Number of doors: {self.doors}\n" \
               f"Type of roof: {self.roof}"


def main():
    print("Welcome to Logan's Car Information App")

    vehicle_type = "car"  #app is designed solely for cars, so car is assumed
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4) of the car: ")
    roof = input("Enter the type of roof (solid or sun roof) of the car: ")

    #are doors either 2 or 4?
    if doors not in ['2', '4']:
        print("Invalid input for doors. Please enter either 2 or 4.")
        return

    #is roof solid or sunroof?
    if roof not in ['solid', 'sun roof']:
        print("Invalid input for roof. Please enter either 'solid' or 'sun roof'.")
        return

    #create Automobile super class object to store user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    #output car information
    print("\nCar Information:")
    print(car)


if __name__ == "__main__":
    main()
