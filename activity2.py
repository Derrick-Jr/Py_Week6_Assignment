class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden.")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Test polymorphism
for v in vehicles:
    print(v.move())
