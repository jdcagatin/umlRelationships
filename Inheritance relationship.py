class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

# Car inherits from Vehicle
class Car(Vehicle):
    def drive(self):
        return f"The {self.brand} is driving fast!"

# --- Running the code ---
# 1. Instantiate a Car object with a brand parameter passed to the Vehicle parent
my_car = Car("Toyota")

# 2. Invoke the inherited attribute and unique subclass method
print(my_car.drive())