class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car model: {self.model}"

    # Example using issubclass (not directly related to object or instance, but demonstrates how to use it)
    def is_electric(self):
        return issubclass(self.__class__, ElectricCar)  # Check if object is subclass of ElectricCar


class ElectricCar(Car):
    def __init__(self, model, battery_range):
        super().__init__(model)  # Call superclass constructor
        self.battery_range = battery_range

    def __str__(self):
        # Override the base class __str__ to include battery range
        return f"Electric Car model: {self.model}, Battery Range: {self.battery_range}km"


# Create objects
car1 = Car("Honda Civic")
car2 = Car("Honda Civic")
electric_car1 = ElectricCar("Tesla Model S", 400)

# Print using __str__
print(car1)  # Output: Car model: Honda Civic
print(electric_car1)  # Output: Electric Car model: Tesla Model S, Battery Range: 400km

# Example using isinstance (not directly related to object or instance, but demonstrates how to use it)
print("Is instance: " + str(isinstance(electric_car1, Car)))  # Output: True (ElectricCar is a subclass of Car)

# Example using is (checks object memory location, not recommended for inheritance checks)
print("The same object: " + str(car1 is car1))  # Output: True (same object)
print("The same object: " + str(car1 is car2))  # Output: False (not the same object)
print("The same model: " + str(car1.model is car2.model))  # Output: False (not the same object)

# Example using super() to call the parent class method (can be useful for chained method calls)
class LuxuryCar(ElectricCar):
    def __init__(self, model, battery_range, features):
        super().__init__(model, battery_range)  # Call ElectricCar constructor
        self.features = features

    def get_info(self):
        # Call parent class __str__ method and add features info using super()
        return super().__str__() + f"\nFeatures: {self.features}"


luxury_car = LuxuryCar("Tesla Model X", 500, "Autopilot, Self-parking")
print(
    luxury_car.get_info())  # Output: Electric Car model: Tesla Model X, Battery Range: 500km\nFeatures: Autopilot, Self-parking
