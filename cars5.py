class Car:
    """A Simpe attempt to represent a car."""
    def __init__(self, make, model,year):
        """Initialize attributes for car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """Return desc name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer to a given value"""
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't rollback an odometer!")
    def increment_odometer(self,miles):
        """Add amount to odometer"""
        self.odometer_reading +=miles

my_used_car=Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_new_car=Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

class ElectricCar(Car):
    """specific for electric"""
    def __init__ (self, make, model,year):
        """init the parent class"""
        super().__init__(make, model,year)
        self.battery_size=40
    def describe_battery(self):
        """battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()