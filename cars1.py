class Step:
    """A Simpe attempt to represent a car."""
    def __init__(self, make, model,year):
        """Initialize attributes for car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return desc name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    my_new_car=Step ('audi','a4', 2024)
    print(my_new_car.get_descriptive_name())